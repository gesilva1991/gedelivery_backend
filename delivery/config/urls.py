from django.contrib import admin
from django.urls import include, path
from config import settings
from django.conf.urls.static import static



urlpatterns = [
    path("admin/", admin.site.urls), 
    path('', include('repositories.urls')), 
    path('auth/', include('autenticacao.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
