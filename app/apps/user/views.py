from django.views.generic import TemplateView


class RegisterPageView(TemplateView):
    template_name = 'components/user/register/register.html'


class LoginPageView(TemplateView):
    template_name = 'components/user/login/login.html'
