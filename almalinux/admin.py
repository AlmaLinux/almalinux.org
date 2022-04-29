from functools import update_wrapper
from typing import List

from django.contrib.admin import AdminSite
from django.template.response import TemplateResponse
from django.urls import path
from django.utils.safestring import SafeString


class AlmaLinuxAdminSite(AdminSite):
    site_title = 'AlmaLinux OS Admin'
    site_header = SafeString('<img src="/static/images/logo.svg" alt="Logo">')

    def get_urls(self) -> List:
        urls: List = []
        urls += super().get_urls()
        urls_insert_pos = len(urls) - 1

        from www.admin import www_admin_urls

        for www_admin_url in www_admin_urls:
            def inner(request):  # type: ignore
                context = {
                    **self.each_context(request),
                    'subtitle': None,
                    'is_nav_sidebar_enabled': False,
                    **(www_admin_url[3] or {})
                }
                request.current_app = self.name

                return TemplateResponse(request, www_admin_url[1], context)

            urls.insert(
                urls_insert_pos,
                path(www_admin_url[0], self.admin_view(inner), name=www_admin_url[2])
            )

        return urls
