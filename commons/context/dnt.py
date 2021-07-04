from typing import Dict

from django.http import HttpRequest


def is_dnt_enabled(request: HttpRequest) -> Dict:
    return {
        'dnt_is_enabled': request.META.get('HTTP_DNT') == '1' or request.META.get('HTTP_SEC_GPC') == '1'
    }
