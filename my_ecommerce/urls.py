from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from my_ecommerce.settings import MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
] + static(settings.MEDIA_URL, document_root=MEDIA_ROOT)
