from django.urls import path
from django.views.generic import RedirectView

from . import views
from .feeds import BlogPostFeed

urlpatterns = [
    path('', views.index, name='index'),
    path('subscribe/thank-you/', views.subscribe_post, name='subscribe_post'),
    path('p/<slug:slug>/', views.content_page, name='page'),
    path('blog/', views.blog_index, name='blog_index'),
    path('blog/page/<int:page_num>/', views.blog_index, name='blog_index_page'),
    path('blog/<slug:slug>/', views.blog_post, name='blog_post'),
    # path('showcase/', views.showcase_index, name='showcase_index'),
    path('contribute/', views.contribute_index, name='contribute_index'),
    path('foundation/members/', views.foundation_members, name='foundation_members'),
    path('feed/', BlogPostFeed(), name='feed'),
    path('media-link/<int:media_id>', views.media_element, name='media_element'),
    path('elevate', views.elevate, name='elevate'),
    path('ELevate', RedirectView.as_view(url='elevate'), name='ELevate'),
    path('certified/amd-ryzen-may2022/', views.certified_index, name="certified_index_page")
]
