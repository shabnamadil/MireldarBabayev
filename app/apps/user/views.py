from django.contrib.auth import (
    authenticate,
    login,
    logout,
)
from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from ..core.models import AboutUs
from .forms import LoginForm


class RegisterPageView(TemplateView):
    template_name = "components/user/register/register.html"

    def get_context_data(self, **kwargs):
        cx = super().get_context_data(**kwargs)
        cx.update({"about": AboutUs.objects.first()})
        return cx

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        return super().dispatch(request, *args, **kwargs)


class LoginPageView(TemplateView):
    template_name = "components/user/login/login.html"

    def get(self, request):
        form = LoginForm()
        context = self.get_context_data(form=form)
        return render(request, self.template_name, context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(
                request,
                email=email,
                password=password,
            )
            if user is not None:
                login(request, user)
                # Check if 'next' URL parameter is present
                next_url = request.POST.get("next")
                if next_url:
                    return redirect(next_url)
                return redirect("home")
            else:
                form.add_error(
                    None,
                    "Invalid email or password",
                )
        context = self.get_context_data(form=form)
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        cx = super().get_context_data(**kwargs)
        cx.update({"about": AboutUs.objects.first()})
        return cx

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        return super().dispatch(request, *args, **kwargs)


def logout_view(request):
    logout(request)
    return redirect("login")
