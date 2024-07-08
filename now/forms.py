from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = ''  # Удаляем помощь для имени пользователя
        self.fields['email'].help_text = ''  # Удаляем помощь для электронной почты
        self.fields['password1'].help_text = None  # Удаляем помощь для первого пароля
        self.fields['password2'].help_text = None  # Удаляем помощь для подтверждения пароля

        # Задаем новый текст помощи для паролей на русском
        self.fields['username'].widget.attrs['placeholder'] = 'Имя пользователя'
        self.fields['email'].widget.attrs['placeholder'] = 'введите почту'
        self.fields['password1'].widget.attrs['placeholder'] = 'Введите пароль'
        self.fields['password2'].widget.attrs['placeholder'] = 'Повторите пароль'

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')
