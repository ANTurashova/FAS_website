from django.db import models  # Без неё не можем обращаться к models
from datetime import date

from django.urls import reverse


class Reviews2(models.Model):
    """Комменты со страницы Кости"""
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Коммент", max_length=5000)
    vkontakte = models.CharField("ВК", max_length=100)
    email = models.EmailField()  # Проверяет, что значение является адресом почты
    parent = models.ForeignKey('self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True)  # Чтобы ответы на комменты писать

    def __str__(self):  # как в админке будут отображаться названия
        return self.name

    class Meta:
        verbose_name = "Коммент"
        verbose_name_plural = "Комменты"


class CourseForm3(models.Model):
    """Запись на курс 3"""

    link_vk = models.CharField("СсылкаВК", max_length=100)
    name = models.CharField("Имя", max_length=100)
    question1 = models.TextField("Вопрос1", max_length=5000)
    question2 = models.TextField("Вопрос2", max_length=5000)

    def __str__(self):  # как в админке будут отображаться названия
        return self.name

    class Meta:
        verbose_name = "Анкета_3"
        verbose_name_plural = "Анкеты_3"
