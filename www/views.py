import datetime
import json

import requests
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator, EmptyPage
from django.core.validators import validate_email
from django.http import Http404
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.utils.timezone import make_aware
from django.utils.translation import gettext as _
from django.views.decorators.cache import never_cache
from django.views.decorators.http import require_POST, require_safe

from almalinux.settings import HUBSPOT_APIKEY, HUBSPOT_SUB_ID
from .models import Backer, PressArticle, BlogPost, Page, FAQEntry, CommercialSupportVendor, ShowcaseFeature, \
    GovernanceMember, MediaElement


# Public views
@require_safe
@never_cache
def index(request: HttpRequest) -> HttpResponse:
    backers = Backer.objects.order_by('-priority').all()
    commercial_support_vendors = CommercialSupportVendor.objects.order_by('-priority').all()
    press_articles = PressArticle.objects.order_by('-priority').all()

    lang_code = request.LANGUAGE_CODE  # type: ignore

    if lang_code != 'en':
        # If the entries does not exist in this language, use EN
        if 0 == FAQEntry.objects.filter(lang=lang_code).count():
            lang_code = 'en'

    faq_entries = FAQEntry.objects.filter(lang=lang_code).order_by('-priority').all()

    return render(request, 'index.html', {
        'backers': backers,
        'commercial_support_vendors': commercial_support_vendors,
        'press_articles': press_articles,
        'faq_entries': faq_entries
    })


@require_POST
def subscribe_post(request: HttpRequest) -> HttpResponse:
    email = request.POST.get('email')

    try:
        validate_email(email)
    except ValidationError:
        return render(request, 'subscribe_post.html', {
            'error': _('Email address is not valid')
        })

    payload = {
        'emailAddress': email,
        'subscriptionId': HUBSPOT_SUB_ID,
        'legalBasis': 'CONSENT_WITH_NOTICE',
        'legalBasisExplanation': 'At users request in almalinux.org website'
    }

    response = requests.request(
        'POST',
        'https://api.hubapi.com/communication-preferences/v3/subscribe',
        data=json.dumps(payload),
        headers={
            'accept': 'application/json',
            'content-type': 'application/json'
        },
        params={'hapikey': HUBSPOT_APIKEY}
    )

    response_data = json.loads(response.text)

    is_error = response_data['status'] == 'error'
    error_message = _('Failed to subscribe to mailing list, please try again later')
    if is_error and 'is already subscribed' in response_data['message']:
        error_message = _('You are already subscribed to this mailing list!')

    return render(request, 'subscribe_post.html', {
        'error': error_message if is_error else None,
    })


# noinspection DuplicatedCode
@require_safe
@never_cache
def content_page(request: HttpRequest, slug: str = None) -> HttpResponse:
    now = make_aware(datetime.datetime.utcnow())

    lang_code = request.LANGUAGE_CODE  # type: ignore

    if lang_code != 'en':
        # If the slug does not exist in this language, use EN
        if 0 == Page.objects.filter(date__lte=now, published=True, lang=lang_code, slug=slug).count():
            lang_code = 'en'

    try:
        page = Page.objects.filter(date__lte=now, published=True, lang=lang_code, slug=slug).get()
    except Page.DoesNotExist:
        raise Http404

    return render(request, 'page/page.html', {
        'page': page
    })


@require_safe
@never_cache
def blog_index(request: HttpRequest, page_num: int = 1) -> HttpResponse:
    if page_num < 1:
        raise Http404

    now = make_aware(datetime.datetime.utcnow())

    lang_code = request.LANGUAGE_CODE  # type: ignore
    if lang_code != 'en':
        # If there are no posts in this language, show EN content
        if 0 == BlogPost.objects.filter(date__lte=now, published=True, lang=lang_code).count():
            lang_code = 'en'

    post_q = (BlogPost.objects
              .filter(date__lte=now, published=True, lang=lang_code)
              .order_by('-date')
              .all())

    paginator = Paginator(post_q, 15)

    try:
        posts = paginator.page(page_num)
    except EmptyPage:
        raise Http404

    return render(request, 'blog/index.html', {
        'posts': posts,
    })


# noinspection DuplicatedCode
@require_safe
@never_cache
def blog_post(request: HttpRequest, slug: str = None) -> HttpResponse:
    now = make_aware(datetime.datetime.utcnow())

    lang_code = request.LANGUAGE_CODE  # type: ignore
    if lang_code != 'en':
        # If the slug does not exist in this language, use EN
        if 0 == BlogPost.objects.filter(date__lte=now, published=True, lang=lang_code, slug=slug).count():
            lang_code = 'en'

    try:
        post = BlogPost.objects.filter(date__lte=now, published=True, lang=lang_code, slug=slug).first()
    except BlogPost.DoesNotExist:
        raise Http404

    return render(request, 'blog/post.html', {
        'post': post
    })


# TODO
# @require_safe
# @never_cache
# def showcase_index(request: HttpRequest) -> HttpResponse:
#     lang_code = request.LANGUAGE_CODE  # type: ignore
#
#     if lang_code != 'en':
#         # If the features does not exist in this language, use EN
#         if 0 == ShowcaseFeature.objects.filter(lang=lang_code).count():
#             lang_code = 'en'
#
#     showcase_features = ShowcaseFeature.objects.filter(lang=lang_code).order_by('-priority').all()
#
#     return render(request, 'showcase/index.html', {
#         'showcase_features': showcase_features,
#     })

@require_safe
@never_cache
def contribute_index(request: HttpRequest) -> HttpResponse:
    return render(request, 'contribute/index.html', {})


@require_safe
@never_cache
def foundation_members(request: HttpRequest) -> HttpResponse:
    board_of_directors = GovernanceMember.objects.filter(type='governance_board').order_by('-priority').all()
    return render(request, 'foundation/members/index.html', {
        'board_of_directors': board_of_directors,
    })


@never_cache
@require_safe
def media_element(_: HttpRequest, media_id: int) -> HttpResponse:
    element = MediaElement.objects.get(id=media_id)

    if element is None:
        raise Http404

    return redirect(element.file.url)


def not_found(request: HttpRequest, exception: Exception) -> HttpResponse:
    return render(request, '404.html', status=404)
