# Django Script for handling app views

from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('view-drink', views.view, name = 'view')
]