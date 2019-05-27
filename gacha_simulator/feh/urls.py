from django.conf.urls import url, include
from django.contrib import admin

from feh import views as feh_views


urlpatterns = [
    url(r'^$', feh_views.index, name='index'),
    url(r'^(?P<pool_name>[^\/]+)/?$', feh_views.gacha, name='gacha'),
    url(r'^(?P<pool_name>[^\/]+)/result/?$', feh_views.gacha_result, name='gacha_result'),
]
