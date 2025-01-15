from django.urls import path
from .views import AuthenticateWithGoogle, LoginView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('google-login/', AuthenticateWithGoogle.as_view(), name='google-login'),
]
