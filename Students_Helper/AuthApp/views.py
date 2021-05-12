from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import login, logout

# exit
def user_logout(request):
    logout(request)
    return redirect('/')
# er
def index(request):
    if request.method == 'POST':
        auth_form = UserLoginForm(data=request.POST)
        if auth_form.is_valid():
            user = auth_form.get_user()
            login(request, user)
            return redirect('/news')
        else:
            messages.error(request, 'Введены некорректные данные. Попробуйте снова')
            return redirect('/')
    else:
        auth_form = UserLoginForm()

# reg
    if request.method == 'POST':
        reg_form = UserRegisterForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            messages.success(request, 'Вы успешно зарегестрировались! Теперь пройдите авторизацию')
        else:
            messages.error(request, 'Введены некорректные данные. Попробуйте снова')
        return redirect('/')
    else:
        reg_form = UserRegisterForm()


    return render(request, 'AuthApp/index.html', {'reg_form': reg_form, 'auth_form': auth_form})


