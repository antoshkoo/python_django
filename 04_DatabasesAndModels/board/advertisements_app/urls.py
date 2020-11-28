from django.urls import path
from .views import AdvertisementDetailView, AdvertisementListView

urlpatterns = [
    path('advertisements/', AdvertisementListView.as_view(), name="advertisement-list"),
    path('advertisements/<int:pk>/', AdvertisementDetailView.as_view(), name="advertisement-detail")
]
