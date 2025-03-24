from django.urls import path

from . import views


urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="RegisterView"),
    path("login/", views.SignInView.as_view(), name="SignInView"),
    path("logout/", views.LogoutView.as_view(), name="LogoutView"),
]
