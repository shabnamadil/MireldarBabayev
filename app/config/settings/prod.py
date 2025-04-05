from .base import *
import dj_database_url

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')

STATIC_ROOT = BASE_DIR / "staticfiles"

INSTALLED_APPS+=['dj_database_url']


DATABASES = {
    'default': dj_database_url.config(default=os.environ['DATABASE_URL'], conn_max_age=600)
}

EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND', '')
EMAIL_HOST = os.environ.get('EMAIL_HOST', '')
EMAIL_PORT = os.environ.get('EMAIL_PORT', '')
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', '')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
