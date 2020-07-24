from django.shortcuts import render, redirect  # redirect поможет перевести пользователя на другую страницу
# from django.http import HttpResponse  # Чтобы выводить строку с текстом
# def home(request):
#     return HttpResponse("<h4>X</h4>")


def home(request):  # request это запрос, который поступает из браузера
    return render(request, 'homepage/home.html')

