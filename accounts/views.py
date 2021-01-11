from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views.generic import CreateView

from . import forms


class LoginView(auth_views.LoginView):
    template_name = "accounts/login.html"


class LogoutView(auth_views.LogoutView):
    template_name = "accounts/logout.html"


class CustomUserCreateView(CreateView):
    template_name = "accounts/register.html"
    form_class = forms.RegistrationForm
    success_message = "You can now login with your new credentials"
    success_url = reverse_lazy("accounts:login")
