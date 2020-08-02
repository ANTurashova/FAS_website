from django.urls import path
from . import views    # . - это значит из этой же директории

urlpatterns = [
#     path('', views.enrollment, name='enrollment'),  # В файле views функция index, views принимает запрос от сервера
    path('2/', views.Review2View.as_view()),
    path('review/2/', views.AddReview2.as_view(), name="add_review2"),
    path('3/', views.Page3View),
    path('review/3/', views.AddCourseForm3.as_view(), name="add_course_form3"),
]
