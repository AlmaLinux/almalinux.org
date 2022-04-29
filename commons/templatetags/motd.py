from typing import Dict, Optional

from django import template
from django.urls import resolve, reverse
from django.utils import translation
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
        href = show_motd.link

        # If not an absolute link, try resolve for current locale
        if href[0:7] != 'http://' and href[0:8] != 'https://':
            request_language = translation.get_language()

            try:
                if request_language == 'en':
                    view, args, kwargs = resolve(href)
                else:
                    view, args, kwargs = resolve('/%s%s' % (request_language, href))

                href = reverse(view, args=args, kwargs=kwargs)
            except:
                # NOOP - can't do anything here...
                pass

        message += (' <a href="%s">' % href) + _('Read more') + '</a>'

    return SafeString(message)
