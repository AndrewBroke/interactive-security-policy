from django import forms
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.models import AbstractUser
from policy.models import Policy

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите пароль'}))
    class Meta:
        model = AbstractUser
        fields = ('username', 'password')

class ChapterForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input-chapter', 'placeholder': 'Название главы' }))
    text = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input-chapter', 'placeholder': 'Название главы'}))

    class Meta:
        model = Policy
        fields = ['title', 'text']