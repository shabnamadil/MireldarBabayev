from django.contrib.auth import authenticate, login
from django.shortcuts import redirect


def get_user_credentials(form, request):
    email = form.cleaned_data['email']
    password = form.cleaned_data['password']
    user = authenticate(request, email=email, password=password)
    return user


def check_next_url(request):
    next_url = request.POST.get('next')
    if next_url:
        return redirect(next_url)
    return redirect('home')


def validate_form(form, request):
    if form.is_valid():
        user = get_user_credentials(form, request)
        if user is not None:
            login(request, user)
            return check_next_url(request)
        else:
            form.add_error(None, 'Invalid email or password')
