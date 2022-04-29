from typing import Dict

from django import template
from django.utils.safestring import SafeString

register = template.Library()


@register.simple_tag(takes_context=True)
def absolute_url_from_relative(context: Dict, relative: str) -> SafeString:
    return SafeString(context['request'].build_absolute_uri(relative))
