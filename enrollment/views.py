# Логика приложения
from django.shortcuts import render, redirect  # redirect поможет перевести пользователя на другую страницу
from django.views.generic.base import View
from django.conf import settings
from django.db import models
from django.db.models import Q, OuterRef, Subquery, Case, When
from django.http import JsonResponse, HttpResponse
from django.views.generic import ListView, DetailView
from .models import Reviews2
from .forms import *


# from django.http import HttpResponse  # Чтобы выводить строку с текстом
# def home(request):
#     return HttpResponse("<h4>X</h4>")


# def enrollment(request):  # request это запрос, который поступает из браузера
#     return render(request, 'enrollment/enroll2.html')


class Review2View(View):
    """Выводит список комментариев"""

    def get(self, request):
        reviews2 = Reviews2.objects.all()  # С помощью .objects забираем записи. reviews2 - переменная, куда эти записи сохранили
        return render(request, "enrollment/enroll2.html", {"reviews2_list": reviews2})  # movie_list = ключ в словаре


class AddReview2(View):
    """"Отправляет форму комментариев"""

    def post(self, request):
        form = Review2Form(request.POST)
        if form.is_valid():  # Проверяем форму на валидность
            form = form.save(commit=False)  # Теперь мы можем внести некие изменения в форму. Вызывая метод save и передавая аргумент commit=False мы говорим о том, что хотим приостановить сохранение формы
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.save()  # И теперь запишем форму в БД.
        return redirect('/enroll/2/')


def Page3View(request):
    return render(request, 'enrollment/enroll3.html')


class AddCourseForm3(View):
    """"Отправляет форму записи на 3 курс"""

    def post(self, request):
        form = CourseForm3Form(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/enroll/3/')
