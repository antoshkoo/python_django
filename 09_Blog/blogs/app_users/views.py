from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.translation import gettext as _
from django.views import View
from django.views.generic import DetailView

from .forms import UserRegisterForm, UserRestorePasswordForm, UserEditForm, ProfileEditForm


def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            raw_password = form.cleaned_data['password1']
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(reverse('posts_list_url'))
    elif request.user.username:
        return redirect(reverse('user_profile_url'))
    else:
        form = UserRegisterForm
    return render(request, 'registration/register.html', context={'form': form})


class UserLoginView(LoginView):
    redirect_authenticated_user = True


class UserLogoutView(LogoutView):
    next_page = 'posts_list_url'


class UserDetailView(DetailView):
    model = User


class UserProfileView(LoginRequiredMixin, View):
    def get(self, request):
        form_user = UserEditForm(instance=request.user)
        form_profile = ProfileEditForm(instance=request.user.profile)
        return render(request, 'auth/user_profile.html', {'form_user': form_user, 'form_profile': form_profile})

    def post(self, request):
        if request.method == 'POST':
            form_user = UserEditForm(instance=request.user, data=request.POST)
            form_profile = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
            if form_user.is_valid() and form_profile.is_valid():
                form_user.save()
                form_profile.save()
        return redirect('user_profile_url')


def restore_password(request):
    if request.method == 'POST':
        form = UserRestorePasswordForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            new_password = User.objects.make_random_password()
            current_user = User.objects.filter(email=user_email).first()
            if current_user:
                current_user.set_password(new_password)
                current_user.save()
            send_mail(
                subject='Password recovery',
                message='Test mail body',
                from_email='admin@company.com',
                recipient_list=[form.cleaned_data['email']]
            )
            return HttpResponse(_('Email with new password was send!'))
    form = UserRestorePasswordForm
    return render(request, 'restore_password.html', context={'form': form})
