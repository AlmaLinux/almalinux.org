from typing import Dict

from django import template
from django.utils.safestring import SafeString

from commons import encore

register = template.Library()


@register.simple_tag(takes_context=True)
def encore_entrypoint_js(context: Dict, entrypoint: str) -> SafeString:
    js = encore.get_js(entrypoint)

    if 'encore_loaded_js' not in context:
        context['encore_loaded_js'] = set()

    if 0 == len(js):
        return SafeString('')

    buffer = ''
    for script in js:
        if script in context['encore_loaded_js']:
            continue

        buffer += '<script src="%s" defer></script>\n' % script
        context['encore_loaded_js'].add(script)

    return SafeString(buffer.strip())


@register.simple_tag(takes_context=True)
def encore_entrypoint_css(context: Dict, entrypoint: str) -> SafeString:
    css = encore.get_css(entrypoint)

    if 'encore_loaded_css' not in context:
        context['encore_loaded_css'] = set()

    if 0 == len(css):
        return SafeString('')

    buffer = ''
    for stylesheet in css:
        if stylesheet in context['encore_loaded_css']:
            continue

        buffer += '<link rel="stylesheet" href="%s">' % stylesheet
        context['encore_loaded_css'].add(stylesheet)

    return SafeString(buffer.strip())
