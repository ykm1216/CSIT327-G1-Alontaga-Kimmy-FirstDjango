from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from .forms import CustomUserCreationForm


def home(request):
    return render(request, 'base.html')


class DashboardLoginView(LoginView):
    template_name = "registration/login.html"

    def get_success_url(self):
        return reverse("dashboard")


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")