from django.urls import path

from .views import NewLoginView, NewLogoutView, user_register, user_profile

urlpatterns = [
    path('login/', NewLoginView.as_view(), name='login'),
    path('logout/', NewLogoutView.as_view(), name='logout'),
    path('register/', user_register, name='register'),
    path('profile/', user_profile, name='profile')
]