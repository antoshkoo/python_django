from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render

from django.utils.translation import gettext as _
from django.views import View

from app_shops.models import Shop, Good, Order, Sale


class MainPageView(View):
    def get(self, request):
        shops = Shop.objects.all()
        cache.get_or_set('shops_cache_key', shops, 30*60)
        return render(request, 'main.html', context={'shops': shops})


class BuyView(LoginRequiredMixin, View):
    def get(self, request, pk):
        user = request.user
        good = Good.objects.get(pk=pk)
        if good and user:
            if Sale.objects.filter(good_id=pk).exists():
                price = Sale.objects.get(good_id=pk).sale_price
            else:
                price = good.price

            if user.profile.balance < price:
                return HttpResponse(_('Please charge your balance!'))
            else:
                user.profile.balance -= price
                user.save()
                Order.objects.create(user=request.user, good=good, price_order=price)
                return HttpResponse(_('Thank you for order!'))
        else:
            return HttpResponse(404)
