from .base import *

DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd59r57o31gva97',
        'USER': 'wtswxmtgwnpldy',
        'PASSWORD': 'y4efOxQMSqeefSzqo1KJdoj55Z',
        'HOST': 'ec2-23-23-210-37.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join('media')
