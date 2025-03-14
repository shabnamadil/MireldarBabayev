from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from utils.helpers.validate_user_form import validate_form

from ..core.models import AboutUs
from .forms import LoginForm


class RegisterPageView(TemplateView):
    template_name = 'components/user/register/register.html'

    def get_context_data(self, **kwargs):
        cx = super().get_context_data(**kwargs)
        cx.update({'about': AboutUs.objects.first()})
        return cx

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)


class LoginPageView(TemplateView):
    template_name = 'components/user/login/login.html'

    def get(self, request):
        form = LoginForm()
        context = self.get_context_data(form=form)
        return render(request, self.template_name, context)

    def post(self, request):
        form = LoginForm(request.POST)
        validate_form(form, request)
        context = self.get_context_data(form=form)
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        cx = super().get_context_data(**kwargs)
        cx.update({'about': AboutUs.objects.first()})
        return cx

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)


def logout_view(request):
    logout(request)
    return redirect('login')
