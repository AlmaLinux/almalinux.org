from django import template
from django.utils.safestring import SafeString

from commons import encore

register = template.Library()


@register.simple_tag()
def encore_entrypoint_js(entrypoint):
    js = encore.get_js(entrypoint)

    if 0 == len(js):
        return ''

    buffer = ''
    for script in js:
        buffer += '<script src="%s" defer></script>\n' % script

    return SafeString(buffer.strip())


@register.simple_tag
def encore_entrypoint_css(entrypoint):
    css = encore.get_css(entrypoint)

    if 0 == len(css):
        return ''

    buffer = ''
    for stylesheet in css:
        buffer += '<link rel="stylesheet" href="%s">' % stylesheet

    return SafeString(buffer.strip())
