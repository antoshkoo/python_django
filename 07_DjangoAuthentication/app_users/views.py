import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import render, redirect

from app_users.forms import AuthForm


def login_view(request):
    sleep_time = datetime.datetime.now().hour

    if sleep_time > 21 or sleep_time < 7:
        return HttpResponse('с 22 до 8 вход запрещен:(')

    elif request.method == 'POST':
        auth_form = AuthForm(request.POST)
        if auth_form.is_valid():
            username = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_superuser:
                    auth_form.add_error('__all__', 'Администраторам вход заапрещен')
                elif user.is_active:
                    login(request, user)
                    return redirect('main')
                else:
                    auth_form.add_error('__all__', 'Пользователь заблокирован')
            else:
                auth_form.add_error('__all__', 'Такого пользователя не существует')

    else:
        auth_form = AuthForm
    context = {'form': auth_form}
    return render(request, 'users/login.html', context=context)


class AnotherLoginView(LoginView):
    template_name = 'users/login.html'


class AnotherLogoutView(LogoutView):
    # template_name = 'users/logout.html'
    next_page = '/'


def logout_view(request):
    logout(request)
    return redirect('main')
