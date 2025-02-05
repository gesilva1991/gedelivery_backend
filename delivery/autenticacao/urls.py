from django.urls import path

from .views import AuthenticateWithGoogle, CheckCookieView, LoginView, LogoutView, SetCookie, Te

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("google-login/", AuthenticateWithGoogle.as_view(), name="google-login"),
    path("check-cookie/", CheckCookieView.as_view(), name="check-cookie"),
    path("set-cookie/", SetCookie.as_view(), name="check-cookie"),
    path("te/", Te.as_view(), name="check-cookie"),

]
