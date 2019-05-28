from django.contrib import admin
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    re_path(r'^some/', views.some),
    re_path(r'^validation/', views.validation),
    re_path(r'^user/', views.user),
    re_path(r'^navigate/', views.navigate),
]
