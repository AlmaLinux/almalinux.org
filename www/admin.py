from typing import List

from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Backer)
admin.site.register(PressArticle)
admin.site.register(Page)
admin.site.register(BlogPost)
admin.site.register(FAQEntry)


# Admin special URLs (path, template, name, context)
www_admin_urls: List = [
    ('manual/', 'admin/manual.html', 'manual', {'title': 'Admin manual'})
]
