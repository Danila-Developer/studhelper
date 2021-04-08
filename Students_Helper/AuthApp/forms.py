from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', "group", 'email', 'password1', 'password2')
    username = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder": "Имя пользователя"}))
    first_name = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder": "Имя"}))
    last_name = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder": "Фамилия"}))
    group = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder": "Группа"}))
    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={"placeholder": "E-mail"}))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={"placeholder": "Пароль"}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={"placeholder": "Подтверждение пароля"}))

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder": "Имя пользователя"}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={"placeholder": "Пароль"}))

