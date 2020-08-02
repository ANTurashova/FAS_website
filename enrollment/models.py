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