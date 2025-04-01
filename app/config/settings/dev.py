from .base import *

SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-i)-r$tm^oz7%jsgjel63s!b1px#snq$=l2)wz0zpx+nx!&c0#v')

DEBUG = True

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
