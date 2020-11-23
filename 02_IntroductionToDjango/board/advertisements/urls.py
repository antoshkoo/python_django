from django.urls import path
from .import views

urlpatterns = [
   path('', views.advertisements_list, name='advertisements_list'),
   path('advertisements/1/', views.advertisement_1, name='advertisements_detail'),
   path('advertisements/2/', views.advertisement_2, name='advertisements_detail'),
   path('advertisements/3/', views.advertisement_3, name='advertisements_detail'),
   path('advertisements/4/', views.advertisement_4, name='advertisements_detail'),
   path('advertisements/5/', views.advertisement_5, name='advertisements_detail'),
]