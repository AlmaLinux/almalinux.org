from typing import Dict

from django import template
from django.urls import resolve, reverse
from django.utils import translation

register = template.Library()


@register.simple_tag(takes_context=True)
def current_path_for_language_code(context: Dict, code: str) -> str:
    view = resolve(context['request'].path)
    request_language = translation.get_language()

    try:
        translation.activate(code)
        url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
    finally:
        translation.activate(request_language)

    return url
