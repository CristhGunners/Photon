"""
Django settings for photon project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vr2^o-hphh0r98^e-6+6r%ia@jdisvz#wll$=*0b!y8lp43&jd'

# Application definition

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
)

THIRD_PARTY_APPS = (
    'easy_thumbnails',
    'taggit',
    'taggit_templatetags',
    'registration',
)

LOCAL_APPS = (
    'photon.apps.user',
    'photon.apps.photo',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'photon.urls'

WSGI_APPLICATION = 'photon.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es-cl'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Templates

TEMPLATE_DIRS = (
    os.path.join('templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)

SOUTH_MIGRATION_MODULES = {
    'taggit': 'taggit.south_migrations',
}

# Auth

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'

AUTH_USER_MODEL = 'user.User'

# Thumbnails Size

THUMBNAIL_ALIASES = {
    '': {
        'avatar': {'size': (150, 150), 'crop': True},
        'home': {'size': (720, 400), 'crop': True},
    },
}

# Registration

ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = False

# Site

SITE_ID = 1

# Backends

AUTHENTICATION_BACKENDS = (
    'photon.apps.user.backends.CaseInsensitiveModelBackend',
)
