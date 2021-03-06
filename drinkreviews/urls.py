# Django Script for handling app views

from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:pk>', views.view, name = 'view'),
    path('<int:pk>/review-drink', views.review, name = 'review'),
    path('create-drink', views.create, name = 'create')
]