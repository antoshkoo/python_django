from django.urls import path

from app_shops.views import MainPageView, BuyView, RefuseView, ShopDetailView

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page_url'),
    path('<int:pk>/', ShopDetailView.as_view(), name='shop_detail_url'),
    path('buy/', BuyView.as_view(), name='buy_url'),
    path('refuse/', RefuseView.as_view(), name='refuse_url'),
]
