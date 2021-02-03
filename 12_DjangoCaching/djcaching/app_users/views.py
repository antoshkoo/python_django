from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView

from app_shops.models import Order
from .forms import UserRegisterForm


class UserRegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('user_profile_url')

    def form_valid(self, form):
        valid = super().form_valid(form)
        login(self.request, self.object)
        return valid


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True


class UserLogoutView(LoginRequiredMixin, LogoutView):
    next_page = 'main_page_url'


class UserProfileView(LoginRequiredMixin, ListView):
    login_url = 'user_login_url'
    template_name = 'users/profile.html'
    context_object_name = 'orders'

    def get_queryset(self):
        queryset = Order.objects.filter(user=self.request.user).select_related('good', 'shop')

        shop_filter = self.request.GET.get('shop', False)
        if shop_filter:
            queryset = queryset.filter(shop_id=shop_filter)

        # cache.delete(make_template_fragment_key('order_history', [self.request.user.username]))
        return queryset
