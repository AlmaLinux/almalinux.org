from typing import Dict, Optional

from django import template
from django.utils.safestring import SafeString
from django.utils.translation import gettext as _

from www.models import MOTD

register = template.Library()


@register.simple_tag(takes_context=True)
def motd(context: Dict) -> Optional[SafeString]:
    show_motd = MOTD.objects.filter(published=True).order_by('-id').first()
    if not show_motd:
        return None

    message = show_motd.text
    if show_motd.link:
        message += (' <a href="%s">' % show_motd.link) + _('Read more') + '</a>'

    return SafeString(message)
