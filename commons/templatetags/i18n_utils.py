from typing import Dict

from django import template
from django.urls import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation

register = template.Library()

RTL_CODES = [
    'ar',  # Arabic
    'arc',  # Aramaic
    'dv',  # Divehi
    'fa',  # Persian
    'ha',  # Hausa
    'he',  # Hebrew
    'khw',  # Khowar
    'ks',  # Kashmiri
    'ku',  # Kurdish
    'ps',  # Pashto
    'ur',  # Urdu
    'yi',  # Yiddish
]


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


@register.simple_tag(takes_context=False)
def text_direction(code: str) -> str:
    if code in RTL_CODES:
        return 'rtl'

    return 'ltr'
