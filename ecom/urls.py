from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL_, document_root="settings.MEDIA_ROOT")
    urlpatterns += static(settings.STATIC_URL, document_root="settings.STATIC_ROOT")
