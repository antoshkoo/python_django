from django.urls import path

from .views import UserLoginView, UserLogoutView, UserDetailView, user_register, user_profile, \
    restore_password

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login_url'),
    path('logout/', UserLogoutView.as_view(), name='logout_url'),
    path('<int:pk>/', UserDetailView.as_view(), name='user_detail_url'),
    path('register/', user_register, name='user_register_url'),
    path('profile/', user_profile, name='user_profile_url'),
    path('restore_password/', restore_password, name='restore_password_url'),
]
