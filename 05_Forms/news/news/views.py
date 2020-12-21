from django.contrib.auth.views import LoginView, LogoutView


class NewLoginView(LoginView):
    template_name = 'login.html'
    redirect_field_name = 'next'
    redirect_authenticated_user = True


class NewLogoutView(LogoutView):
    next_page = 'news-list'