"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path, include
import mainapp.views as mainapp

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    re_path(r'^', include('mainapp.urls', namespace='main')),
    re_path(r'^auth/', include('authapp.urls', namespace='auth')),
    re_path(r'^basket/', include('basketapp.urls', namespace='basket')),
    re_path(r'^myadmin/', include('adminapp.urls', namespace='myadmin')),
    # теперь вызываются через пространство имён
    # r'^адрес$'- формируем адрес, контролер, url teg
    # re_path(r'^$', mainapp.index, name='index'),
    # re_path(r'^contacts/$', mainapp.contacts, name='contacts'),
    # re_path(r'^catalog/$', mainapp.catalog, name='catalog'),

    re_path(r'^auth/verify/google/oauth2/', include("social_django.urls", namespace="social")),

    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
