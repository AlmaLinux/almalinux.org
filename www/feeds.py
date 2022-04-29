from datetime import datetime

from django.contrib.syndication.views import Feed
from django.urls import reverse
from django.utils.timezone import make_aware

from .models import BlogPost

class BlogPostFeed(Feed):
    title = 'AlmaLinux OS Blog Feed'
    link = '/feed/'
    description = 'Latest blog posts from almalinux.org'

    def items(self):
        now = make_aware(datetime.utcnow())
        return BlogPost.objects.filter(date__lte=now, published=True, lang='en').order_by('-date')[:50]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.excerpt

    def item_link(self, item):
        return reverse('blog_post', args=[item.slug])

    def item_pubdate(self, item):
        return item.date
