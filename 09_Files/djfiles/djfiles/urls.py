from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_media.urls')),
    path('goods/', include('app_goods.urls')),
    path('files/', include('app_media.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
