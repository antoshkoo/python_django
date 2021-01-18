from django.urls import path
from .views import update_prices, ItemDetailView

urlpatterns = [
    path('update_prices/', update_prices, name='update_prices'),
]
