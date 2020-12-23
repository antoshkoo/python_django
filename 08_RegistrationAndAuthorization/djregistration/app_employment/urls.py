from django.urls import path

from .views import vacancy_list, resume_list

urlpatterns = [
    path('vacancy/', vacancy_list, name='vacancy_list'),
    path('resume/', resume_list, name="resume_list")
]