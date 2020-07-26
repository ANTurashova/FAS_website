from django import forms
# from snowpenguin.django.recaptcha3.fields import ReCaptchaField

from .models import Reviews, Rating, RatingStar


class ReviewForm(forms.ModelForm):  # Наследуемся от forms.ModelForm
    """Форма отзывов"""  # На основе класса ModelForm будем строить форму, т.е. форма будет построены от модели. В этой форме будут содержаться те поля, которые мы укажем.
                         # Так же мы можем создавать просто формы, наследуясь от класса формс и указывая вручную поля, точно так же, как в мы указываем их в моделях
    # captcha = ReCaptchaField()

    class Meta:
        model = Reviews  # Указываем, от какой модели нам нужно стоить форму
        fields = ("name", "email", "text")#, "captcha")  # Указываем поля из модели, которые мы хотим видеть в форме
        # widgets = {  #
        #     "name": forms.TextInput(attrs={"class": "form-control border"}),
        #     "email": forms.EmailInput(attrs={"class": "form-control border"}),
        #     "text": forms.Textarea(attrs={"class": "form-control border"})
        # }


class RatingForm(forms.ModelForm):
    """Форма добавления рейтинга"""
#     star = forms.ModelChoiceField(
#         queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None
#     )
#
#     class Meta:
#         model = Rating
#         fields = ("star",)