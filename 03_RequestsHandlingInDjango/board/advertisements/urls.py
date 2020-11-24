from django.urls import path

from . import views

urlpatterns = [
    path('advertisements/', views.Advertisements.as_view(), name='advertisement_list'),
    path('about/', views.About.as_view(), name='about'),
    path('contacts/', views.Contacts.as_view(), name='contacts'),
    path('', views.Home.as_view(), name='home'),
]
