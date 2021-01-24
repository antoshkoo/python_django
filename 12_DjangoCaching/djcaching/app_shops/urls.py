from django.urls import path

from app_shops.views import MainPageView, BuyView

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page_url'),
    path('buy/<int:pk>/', BuyView.as_view(), name='buy_url')
]