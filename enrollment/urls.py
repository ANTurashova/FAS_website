from django.urls import path
from . import views    # . - это значит из этой же директории

urlpatterns = [
#     path('', views.enrollment, name='enrollment'),  # В файле views функция index, views принимает запрос от сервера
    path('', views.Review2View.as_view()),
    path('review/1/', views.AddReview2.as_view(), name="add_review2"),
]
