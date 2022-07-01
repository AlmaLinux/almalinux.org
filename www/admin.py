from typing import List
from django.contrib import admin
from django.contrib.admin.decorators import display

from .models import *


# Register your models here.
class MediaElementAdmin(admin.ModelAdmin):
    model = MediaElement
    list_display = ['__str__', 'file_permalink', ]

    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        self.request = None

    def get_queryset(self, request):
        self.request = request
        return super().get_queryset(request)

    @display(description='Permalink')
    def file_permalink(self, obj):
        from django.urls import reverse
        return self.request.build_absolute_uri(reverse('media_element', kwargs={'media_id': obj.id}))


class BlogPostAdmin(admin.ModelAdmin):
    model = BlogPost

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        # print(request.user)
        super().save_model(request, obj, form, change)


admin.site.register(UserProfile)
admin.site.register(Backer)
admin.site.register(CommercialSupportVendor)
admin.site.register(PressArticle)
admin.site.register(Page)
admin.site.register(FAQEntry)
admin.site.register(ShowcaseFeature)
admin.site.register(GovernanceMember)
admin.site.register(MediaElement, MediaElementAdmin)
admin.site.register(MOTD)
admin.site.register(BlogPost, BlogPostAdmin)

# Admin special URLs (path, template, name, context)
www_admin_urls: List = [
    ('manual/', 'admin/manual.html', 'manual', {'title': 'Admin manual'})
]
