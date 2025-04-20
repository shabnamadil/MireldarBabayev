from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from ..core.models import AboutUs


class RegisterPageView(TemplateView):
    template_name = 'components/user/register/register.html'

    def get_context_data(self, **kwargs):
        cx = super().get_context_data(**kwargs)
        cx.update({'about': AboutUs.objects.first()})
        return cx


class LoginPageView(TemplateView):
    template_name = 'components/user/login/login.html'

    def get_context_data(self, **kwargs):
        cx = super().get_context_data(**kwargs)
        cx.update({'about': AboutUs.objects.first()})
        return cx
