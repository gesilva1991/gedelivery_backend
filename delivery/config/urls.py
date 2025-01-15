from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls), 
    path('', include('repositories.urls')), 
    path('auth/', include('autenticacao.urls')),
]
