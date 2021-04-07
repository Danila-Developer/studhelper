from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

def index(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегестрировались! Теперь пройдите авторизацию')
        else:
            messages.error(request, 'Ошибка регистрации. Попробуйте снова')
        return redirect('/')
    else:
        form = UserRegisterForm()
    return render(request, 'AuthApp/index.html', {'form': form})


