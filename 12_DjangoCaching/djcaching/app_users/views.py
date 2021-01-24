from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect

from django.views import View

from app_shops.models import Shop
from .forms import UserRegisterForm


class UserRegisterView(View):
    def get(self, request):
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
    redirect_authenticated_user = False


class UserLogoutView(LoginRequiredMixin, LogoutView):
    next_page = 'user_register_url'


class UserProfileView(LoginRequiredMixin, View):
    def get(self, request):
        shops = Shop.objects.all()
        return render(request, 'users/profile.html', context={'shops': shops})
