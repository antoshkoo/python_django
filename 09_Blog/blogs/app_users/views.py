from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.forms import inlineformset_factory
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import DetailView

from .models import Profile
from .forms import UserRegisterForm, UserProfileForm, UserRestorePasswordForm


def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            raw_password = form.cleaned_data['password1']
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserRegisterForm
    return render(request, 'registration/register.html', context={'form': form})


class UserLoginView(LoginView):
    redirect_field_name = 'next'
    redirect_authenticated_user = True


class UserLogoutView(LogoutView):
    next_page = '/'


class UserDetailView(DetailView):
    model = User


@login_required(login_url='login_url')
def user_profile(request):
    user = User.objects.get(pk=request.user.id)
    UserProfileFormSet = inlineformset_factory(User, Profile, fields=('__all__'), can_delete=False)
    if request.method == 'POST':
        form_user = UserProfileForm(request.POST)
        form_profile = UserProfileFormSet(request.POST, request.FILES, instance=user)
        if form_profile.is_valid() and form_user.is_valid():
            form_profile.save()
            user.first_name = form_user.cleaned_data['first_name']
            user.last_name = form_user.cleaned_data['last_name']
            user.save()
            return redirect('user_profile_url')
    else:
        form_profile = UserProfileFormSet(instance=user)
        form_user = UserProfileForm(instance=user)
    return render(request, 'auth/user_profile.html', context={'form_profile': form_profile, 'form_user': form_user})


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
            return HttpResponse('Email with new password was send!')
    form = UserRestorePasswordForm
    return render(request, 'restore_password.html', context={'form': form})
