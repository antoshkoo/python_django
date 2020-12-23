from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render

from .forms import RegisterForm
from .models import Profile


class NewLoginView(LoginView):
    template_name = 'login.html'
    redirect_field_name = 'next'
    redirect_authenticated_user = True


class NewLogoutView(LogoutView):
    next_page = 'news-list'


def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(
                user=user,
                city=form.cleaned_data['city'],
                phone=form.cleaned_data['phone'],
                date_of_birth=form.cleaned_data['date_of_birth'],
                discount_card=form.cleaned_data['discount_card']
            )
            username = form.cleaned_data['username']
            raw_password = form.cleaned_data['password1']
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('news-list')
    else:
        form = RegisterForm
    return render(request, 'register.html', context={'form': form})


@login_required(login_url='login')
def user_profile(request):
    return render(request, 'profile.html')
