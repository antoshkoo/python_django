from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse

from django.utils.translation import gettext as _
from django.views import View
from django.views.generic import ListView, DetailView

from app_shops.models import Shop, Good, Order, Sale, Promotion


class MainPageView(ListView):
    model = Shop
    template_name = 'main.html'
    context_object_name = 'shops'


class ShopDetailView(DetailView):
    model = Shop
    template_name = 'shops/shop_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        shop = context['shop']

        goods = cache.get_or_set(f'goods {shop.id}', Good.objects.filter(shop_id=shop.id, sales__sale_price=None), 600)
        sales = cache.get_or_set(f'sales {shop.id}', Sale.objects.filter(shop_id=shop.id).select_related('good'), 600)
        promotions = cache.get_or_set(f'promotions {shop.id}', Promotion.objects.filter(shop_id=shop.id), 600)

        context['goods'] = goods
        context['sales'] = sales
        context['promotions'] = promotions
        return context


class BuyView(LoginRequiredMixin, View):
    def post(self, request):
        obj = request.POST
        good = get_object_or_404(Good, pk=obj['good_id'])

        try:
            price = Sale.objects.get(good_id=obj['good_id']).sale_price
        except Sale.DoesNotExist:
            price = good.price

        total_cost = price * int(obj['quantity'])

        if request.user.profile.balance < total_cost:
            return HttpResponse(_('Please charge your balance!') +
                                f' <a href="{reverse("main_page_url")}">Go to main</a>')
        else:
            request.user.profile.balance -= total_cost
            request.user.save()
            Order.objects.create(user=request.user,
                                 good=good,
                                 price_order=price,
                                 quantity=int(obj['quantity']),
                                 shop_id=good.shop_id,
                                 )
            return HttpResponse(_(f'Thank you for order!') +
                                f' <a href="{reverse("user_profile_url")}">Go to profile</a>')


class RefuseView(LoginRequiredMixin, View):
    def post(self, request):
        obj = request.POST
        order = get_object_or_404(Order, pk=obj['order'])

        if order.user == request.user:
            request.user.profile.balance += order.total_cost()
            request.user.save()
            order.delete()
            return HttpResponse(_(f'Your order was refused! Order\'s amount was return on your balance') +
                                f' <a href="{reverse("user_profile_url")}">Go to profile</a>')
        else:
            return HttpResponse(_('Order not found'))