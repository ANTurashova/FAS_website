# Логика приложения
from django.conf import settings
from django.db import models
from django.db.models import Q, OuterRef, Subquery, Case, When
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from django.shortcuts import render, redirect  # redirect поможет перевести пользователя на другую страницу

from .models import Movie, Category, Actor, Genre, Rating, Reviews
from .forms import ReviewForm, RatingForm


# def Movies(request):  # Просто подключение html странички
#     return render(request, 'test_movies/movie_list.html')


# class GenreYear:
#     """Жанры и года выхода фильмов"""
#
#     def get_genres(self):
#         return Genre.objects.all()
#
#     def get_years(self):
#         return Movie.objects.filter(draft=False).values("year")
#
#
# def get_client_ip(request):
#     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#     if x_forwarded_for:
#         ip = x_forwarded_for.split(',')[0]
#     else:
#         ip = request.META.get('REMOTE_ADDR')
#     return ip


# class MoviesView(View):
#     """Список фильмов"""
#     def get(self, request):
#         movies = Movie.objects.all()  # В переменную movies сохраняем все записи
#         return render(request, "test_movies/movie_list.html", {"movie_list": movies})  # movie_list = ключ в словаре
class MoviesView(ListView):
    """Список фильмов"""
    model = Movie  # Модель
#     queryset = Movie.objects.all()  # Вывод всего
    queryset = Movie.objects.filter(draft=False)  # draft это черновик из Movie, чернровики же не выводим
    # template_name : джанго автоматически подставляет суффикс к шаблону. Берёт имя модели "movie" и добавляет "_list"


# class MovieDetailView(View):
#     """Полное описание фильма"""
#     def get(self, request, slug):  # Принимает get-запрос, в который передаётсяя request и pk(=некое число из url)
#         movie = Movie.objects.get(url=slug)  # Делаем запрос в БД, получая 1 запись, у  которрой id сравниваем с pk
#         return render(request, "test_movies/movie_detail.html", {"movie": movie})
class MovieDetailView(DetailView):
    """Полное описание фильма"""
    model = Movie
    # queryset = Movie.objects.filter(draft=False)
    slug_field = "url"
    # template_name: джанго автоматически подставляет суффикс к шаблону. Берёт имя модели "movie" и добавляет "_detail"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["star_form"] = RatingForm()
    #     context["form"] = ReviewForm()
    #     return context


class AddReview(View):
    """Класс для отправки отзывов"""
    def post(self, request, pk):
        form = ReviewForm(request.POST)  # Используя форму из forms.py и передавая в неё request.POST, Django заполнит форму данными, которые пришли из запроса
        movie = Movie.objects.get(id=pk)  # Делаем запрос в БД на получение записей и находим фильм по id, получаем объект movie
        if form.is_valid():  # Проверяем форму на валидность
            # pass
            form = form.save(commit=False)  # Вызывая метод save и передавая аргумент commit=False мы говорим о том, что хотим приостановить сохранение формы
                                            # Теперь мы можем внести некие изменения в форму
            # form.movie_id = pk  # В  поле movie нужно указать фильм, к которому нужно привязаться.
            # Но так как у нас есть только pk(т.е. id фильма), напрямую в "form.movie = pk" мы не можем передать данное число, т.к.
            # передадим объект фильма. Можем через "_id" указать наше значение. Если глянуть в БД, там как раз есть movie_id.
            if request.POST.get("parent", None):  # Ключ parent - это имя поля (родитель), если его нет будет None, если есть:
                form.parent_id = int(request.POST.get("parent"))  # из поля parent_id (нам нужно именно число _id) достаём значение ключа parent. int делает значение числовым
            form.movie = movie  # В форме в поле movie присваиваем полученный выше из БД объект movie
            form.save()  # И теперь запишем в БД форму.
        # return redirect("/test_movies/")
        return redirect(movie.get_absolute_url())  # Адрес фильма, чтобы перенаправило на ту же самую страницу, откуда отправился отзыв
        # print(request.POST)



# class ActorView(GenreYear, DetailView):
#     """Вывод информации о актере"""
#     model = Actor
#     template_name = 'movies/actor.html'
#     slug_field = "name"
#
#
# class FilterMoviesView(GenreYear, ListView):
#     """Фильтр фильмов"""
#     paginate_by = 5
#
#     def get_queryset(self):
#         queryset = Movie.objects.filter(
#             Q(year__in=self.request.GET.getlist("year")) |
#             Q(genres__in=self.request.GET.getlist("genre"))
#         ).distinct()
#         return queryset
#
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         context["year"] = ''.join([f"year={x}&" for x in self.request.GET.getlist("year")])
#         context["genre"] = ''.join([f"genre={x}&" for x in self.request.GET.getlist("genre")])
#         return context
#
#
# class JsonFilterMoviesView(ListView):
#     """Фильтр фильмов в json"""
#
#     def get_queryset(self):
#         queryset = Movie.objects.filter(
#             Q(year__in=self.request.GET.getlist("year")) |
#             Q(genres__in=self.request.GET.getlist("genre"))
#         ).distinct().values("title", "tagline", "url", "poster")
#         return queryset
#
#     def get(self, request, *args, **kwargs):
#         queryset = list(self.get_queryset())
#         return JsonResponse({"movies": queryset}, safe=False)
#
#
# class AddStarRating(View):
#     """Добавление рейтинга фильму"""
#
#     def get_client_ip(self, request):
#         x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#         if x_forwarded_for:
#             ip = x_forwarded_for.split(',')[0]
#         else:
#             ip = request.META.get('REMOTE_ADDR')
#         return ip
#
#     def post(self, request):
#         form = RatingForm(request.POST)
#         if form.is_valid():
#             Rating.objects.update_or_create(
#                 ip=self.get_client_ip(request),
#                 movie_id=int(request.POST.get("movie")),
#                 defaults={'star_id': int(request.POST.get("star"))}
#             )
#             return HttpResponse(status=201)
#         else:
#             return HttpResponse(status=400)
#
#
# class Search(ListView):
#     """Поиск фильмов"""
#     paginate_by = 3
#
#     def get_queryset(self):
#         return Movie.objects.filter(title__icontains=self.request.GET.get("q"))
#
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         context["q"] = f'q={self.request.GET.get("q")}&'
#         return context