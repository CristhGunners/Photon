from .base import *

DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join('media')

# Email

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'host@gmail.com'
EMAIL_HOST_PASSWORD = '*****'

REGISTRATION_OPEN = False
