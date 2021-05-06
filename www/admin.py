from django.contrib import admin

# from django.conf.urls import url

# Register your models here.

# admin.site.register(...)

# Admin customizations
frontpage_admin_urls = [
    # url(r'^tweet/process/$', admin.site.admin_view(...CUSTOM_ADMIN_VIEW))
]

_original_urls_reader = admin.site.get_urls
admin.site.get_urls = lambda: (_original_urls_reader() + frontpage_admin_urls)
