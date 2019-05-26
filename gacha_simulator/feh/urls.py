from django.conf.urls import url, include
from django.contrib import admin

from feh import views as feh_views


urlpatterns = [
    url(r'^$', feh_views.index),
    url(r'^gacha/(?P<pool_name>.+)/?$', feh_views.gacha, name='gacha'),
    url(r'^gacha_result/$', feh_views.gacha_result, name='gacha_result'),
]
