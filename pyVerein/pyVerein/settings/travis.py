"""
Django settings for BA project.
Generated by 'django-admin startproject' using Django 1.11.1.
For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []


# Application definition

WSGI_APPLICATION = 'pyVerein.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'travis_ci_db',
            'USER': 'postgres',
            'PASSWORD': '',
            'HOST': '127.0.0.1',
        }
    }

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

SENDFILE_URL = '/sendfile/'
SENDFILE_ROOT = os.path.join(BASE_DIR, 'sendfile')
SENDFILE_BACKEND = 'sendfile.backends.development'