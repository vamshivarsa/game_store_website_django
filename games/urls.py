from django.contrib import admin
from django.urls import path,re_path
from .import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    re_path(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='index'),
]
