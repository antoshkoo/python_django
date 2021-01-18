from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path
from app_goods.views import item_list, ItemDetailView

urlpatterns = [
    path('logic/', include('app_logic.urls')),
    path('goods/', include('app_goods.urls')),
    path('users/', include('app_users.urls')),
    path('', include('app_pages.urls')),
    path('i18n', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    path('goods/items/', item_list, name='item_list'),
    path('goods/<int:pk>/', ItemDetailView.as_view(), name='item_detail'),
)
