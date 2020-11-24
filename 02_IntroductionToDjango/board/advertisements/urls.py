from django.urls import path
from .import views

urlpatterns = [
   path('', views.advertisements_list, name='advertisements_list'),
   path('advertisements/1/', views.advertisement_1, name='advertisements_detail_1'),
   path('advertisements/2/', views.advertisement_2, name='advertisements_detail_2'),
   path('advertisements/3/', views.advertisement_3, name='advertisements_detail_3'),
   path('advertisements/4/', views.advertisement_4, name='advertisements_detail_4'),
   path('advertisements/5/', views.advertisement_5, name='advertisements_detail_5'),
   path('contacts/', views.contacts, name='contacts'),
   path('about/', views.about, name='about'),
   path('categories/', views.categories, name='categories'),
   path('regions/', views.Regions.as_view()),
]