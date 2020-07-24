from django.contrib import admin
from django.urls import path, include
from . import views    # . - это значит из этой же директории

urlpatterns = [
    path('', views.home, name='home'),  # В файле views функция index, views принимает запрос от сервера
]
