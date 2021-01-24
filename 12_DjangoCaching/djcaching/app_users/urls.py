from django.urls import path

from .views import UserProfileView, UserRegisterView, UserLogoutView, UserLoginView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user_register_url'),
    path('login/', UserLoginView.as_view(), name='user_login_url'),
    path('logout/', UserLogoutView.as_view(), name='user_logout_url'),
    path('profile/', UserProfileView.as_view(), name='user_profile_url'),
]