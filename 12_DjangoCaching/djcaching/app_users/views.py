from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect

from django.views import View

from .forms import UserRegisterForm


class UserRegisterView(View):
    def get(self, request):
        if request.user.username:
            return redirect('user_profile_url')
        else:
            form = UserRegisterForm
            return render(request, 'users/register.html', context={'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('user_profile_url')


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True


class UserLogoutView(LoginRequiredMixin, LogoutView):
    next_page = 'main_page_url'


class UserProfileView(LoginRequiredMixin, View):
    login_url = 'user_login_url'

    def get(self, request):
        return render(request, 'users/profile.html')
