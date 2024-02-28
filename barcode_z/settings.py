from pathlib import Path
import os
from datetime import timedelta
from re import T
from .config import *

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = SECRET_KEY

DEBUG = False

ALLOWED_HOSTS = ALLOWED_HOSTS

INSTALLED_APPS = [
    'diplom',
    'ajax_datatable',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic',
    'rest_framework', 
    'widget_tweaks',
    # 'bootstrap_modal_forms',
    'django_htmx',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_auto_logout.middleware.auto_logout',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django_htmx.middleware.HtmxMiddleware'
]

ROOT_URLCONF = 'barcode_z.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
            'libraries': {
                'custom_tags':'diplom.template_tags.custom_tags'
            }
        },
    },
]

WSGI_APPLICATION = 'barcode_z.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': DB_ENGINE,
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST
    }
}

FILE_CHARSET = FILE_CHARSET


# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
#     ]
# }


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = LANGUAGE_CODE

TIME_ZONE = TIME_ZONE

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

AUTO_LOGOUT = {'IDLE_TIME': timedelta(minutes=AUTO_LOGOUT)}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'