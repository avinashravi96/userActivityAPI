from django.urls import include, path
from django.conf.urls import url 
from rest_framework import routers
from . import views

urlpatterns = [
    url(r'^api/activity$', views.activity_list),
    url(r'^api/activity/(?P<pk>[0-9]+)$', views.activity_detail),
    url(r'^api/user$', views.user_list),
    url(r'^api/user/(?P<pk>[0-9]+)$', views.user_detail),
    url(r'^api/members$', views.members_list),
]