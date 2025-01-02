from django.shortcuts import render

def custom_404(request, exception):
    return render(request, 'components/core/errors/404.html', status=404)

def custom_500(request):
    return render(request, 'components/core/errors/500.html', status=500)
