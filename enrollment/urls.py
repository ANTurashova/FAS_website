from django.urls import path
from . import views    # . - это значит из этой же директории

urlpatterns = [
    path('', views.enrollment, name='enrollment'),  # В файле views функция index, views принимает запрос от сервера
]
