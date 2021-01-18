from django.urls import path

from app_users.views import restore_password, login_view, logout_view, register_view, user_account, update_user_account

urlpatterns = [
    path('login/', login_view, name='login_url'),
    path('logout/', logout_view, name='logout_url'),
    path('register/', register_view, name='user_register_url'),
    path('account/', user_account, name='user_account_url'),
    path('account_edit/', update_user_account, name='user_account_edit_url'),
    path('restore_password/', restore_password, name='restore_password_url'),
]
