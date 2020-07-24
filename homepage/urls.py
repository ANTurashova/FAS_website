from django.urls import path
from . import views    # . - это значит из этой же директории

urlpatterns = [
    path('', views.home, name='home'),  # В файле views функция index, views принимает запрос от сервера
]
