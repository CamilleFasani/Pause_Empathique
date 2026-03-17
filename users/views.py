from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import DeleteView, DetailView, UpdateView

from .forms import CustomAuthenticationForm, RegisterForm, UserProfileForm
from .models import User


class CustomLoginView(LoginView):
    template_name = "users/login.html"
    authentication_form = CustomAuthenticationForm
    redirect_authenticated_user = True


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                login(request, user)
                return redirect(settings.LOGIN_REDIRECT_URL)
            except Exception:
                messages.error(request, "Une erreur est survenue. Veuillez réessayer.")
    else:
        form = RegisterForm()
    return render(request, "users/register.html", context={"form": form})


class UserProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "users/profile_detail.html"

    def get_object(self):
        return self.request.user


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = "users/profile_update.html"
    success_url = reverse_lazy("profile")

    def get_object(self):
        return self.request.user


class UserProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = "users/profile_delete.html"
    success_url = reverse_lazy("home")

    def get_object(self):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        messages.success(
            request, "Votre compte et toutes vos données ont été supprimés."
        )
        logout(request)
        return super().delete(request, *args, **kwargs)
