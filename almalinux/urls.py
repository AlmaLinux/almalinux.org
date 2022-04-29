"""almalinux URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from typing import List

from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.views.i18n import JavaScriptCatalog

handler404 = 'www.views.not_found'

urlpatterns: List = []
urlpatterns += i18n_patterns(path('', include('www.urls')), prefix_default_language=False)

urlpatterns += [
    path('admin/', admin.site.urls),
    path('favicon.ico', RedirectView.as_view(url='/static/fav/favicon.ico'))
]

urlpatterns += i18n_patterns(path(
    'jsi18n/',
    JavaScriptCatalog.as_view(),
    name='javascript-catalog'
), prefix_default_language=False)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
