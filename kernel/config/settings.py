# -*- coding: utf-8 -*-

import os
from datetime import timedelta

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = os.getenv('DEBUG') == 'True'

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    # 'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # LIBS:
    'graphene_django',
    'corsheaders',

    # APPS:
    'tasks',
    'users',
    'project',
    'organisation',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                'django.template.context_processors.request',
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'db'),
        'USER': os.getenv('DB_USER', 'developer'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'Passw0rd33'),
        'HOST': os.getenv('DB_HOST', 'db'),
        # 'PORT': '5432',
    }
}

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

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',  
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.timeweb.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'no-reply@makridenko.ru'  
EMAIL_HOST_PASSWORD = '#^57-#O.g_4Y4N'  
DEFAULT_FROM_EMAIL = 'no-reply@makridenko.ru'
# EMAIL_USE_TLS = True

LANGUAGE_CODE = 'en-US'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'webclient/static'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

GRAPHENE = {
    "SCHEMA": "config.schema.schema"
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
GRAPHQL_JWT = {
    "JWT_COOKIE_NAME": "auth",
    "JWT_REFRESH_TOKEN_COOKIE_NAME": "auth-refresh",
    "JWT_COOKIE_SECURE": os.getenv("DEBUG") == "False",
    "JWT_COOKIE_PATH": "/",
    "JWT_COOKIE_DOMAIN": None,
    "JWT_COOKIE_SAMESITE": "Lax",
    "JWT_VERIFY_EXPIRATION": True,
    "WT_ALLOW_REFRESH": True,
    "JWT_EXPIRATION_DELTA": timedelta(minutes=5),
    "JWT_REFRESH_EXPIRATION_DELTA": timedelta(days=7),
}

try:
    from .local_settings import *
except ImportError:
    pass
