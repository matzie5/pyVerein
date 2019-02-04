"""pyVerein URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.urls import re_path
from django.views.static import serve
from two_factor.urls import urlpatterns as tf_urls

urlpatterns = i18n_patterns(
    url(r'^', include('app.urls')),
    url(r'^account/', include('account.urls'), name='account'),
    url(r'^members/', include('members.urls'), name='members'),
    url(r'^finance/', include('finance.urls'), name='finance'),
    url(r'^reporting/', include('reporting.urls'), name='reporting'),
    url(r'^tasks/', include('tasks.urls'), name='tasks'),
    url(r'^admin/', admin.site.urls),
    url(r'', include(tf_urls)),
                            )
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
