from django.core.management.base import BaseCommand
from markdownify import markdownify as md

from www.models import BlogPost, Page


class Command(BaseCommand):
    def handle(self, *args, **options):
        posts = BlogPost.objects.all()

        for post in posts:
            post.content_md = md(post.content.html)
            post.save()

        pages = Page.objects.all()

        for page in pages:
            page.content_md = md(page.content.html)
            page.save()
