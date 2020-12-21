from django.urls import path
from app_users.views import login_view, AnotherLoginView, logout_view, AnotherLogoutView

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('another-login/', AnotherLoginView.as_view(), name='another-login'),
    path('another-logout/', AnotherLogoutView.as_view(), name='another-logout'),
]
