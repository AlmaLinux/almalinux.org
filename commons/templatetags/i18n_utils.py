from typing import Dict

from django import template
from django.urls import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation

register = template.Library()


@register.simple_tag(takes_context=True)
def current_path_for_language_code(context: Dict, code: str) -> str:
    try:
        view = resolve(context['request'].path)
    except Resolver404:
        view = resolve('/')

    request_language = translation.get_language()

    try:
        translation.activate(code)
        url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
    finally:
        translation.activate(request_language)

    return url
