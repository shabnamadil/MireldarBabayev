from .base import *

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

CSRF_TRUSTED_ORIGINS=['http://13.60.211.242', 'https://13.60.211.242'] # change after domain available

EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND', '')
EMAIL_HOST = os.environ.get('EMAIL_HOST', '')
EMAIL_PORT = os.environ.get('EMAIL_PORT', '')
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', '')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
