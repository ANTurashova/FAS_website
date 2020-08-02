from django import forms
from .models import *


class Review2Form(forms.ModelForm):  # Наследуемся от forms.ModelForm
    """Форма комментов"""
    # captcha = ReCaptchaField()

    class Meta:
        model = Reviews2  # Указываем, от какой модели нам нужно стоить форму
        fields = ("name", "text", "vkontakte", "email")#, "captcha")  # Указываем поля из модели, которые мы хотим видеть в форме
