from django.conf.urls import url, include
from .views import TasklistCreateView, TasklistDetailsView, TaskCreateView, TaskDetailsView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers, serializers, viewsets
from rest_framework import generics
from rest_framework import viewsets, routers  
from .views import TagTypeViewSet
from .views import TagViewSet
from .views import RegisterView
from django.conf import urls


urlpatterns = {
    url(r'^todolists/$', TaskCreateView.as_view(), name="create"),
    url(r'^todolists/(?P<pk>[0-9]+)/$', TaskDetailsView.as_view(), name="detail"),
}

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns = {
    url(r'^todolists/$', TasklistCreateView.as_view(), name="lists"),
    url(r'^todolists/(?P<pk>[0-9]+)/$', TasklistDetailsView.as_view(), name="list-detail"),
    url(r'^todolists/(?P<list_id>[0-9]+)/tasks', TaskCreateView.as_view(), name="tasks"),
    url(r'^todolists/(?P<list_id>[0-9]+)/tasks/(?P<pk>[0-9]+)', TaskDetailsView.as_view(), name="task-detail"),
	url(r'^todolists/tag/$', TagViewSet.as_view(), name="tag"),
	url(r'^todolists/tag_type/$', TagTypeViewSet.as_view(), name="tag-type"),
	url(r'^todolists/register/$', RegisterView.as_view(), name="register"),
}

urlpatterns = format_suffix_patterns(urlpatterns)