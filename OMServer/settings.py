"""
Django settings for OMServer project.

Generated by 'django-admin startproject' using Django 1.11.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from django.urls import reverse_lazy

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'odf12^qah=%f1ofw^6#+l9pr#dh!n=@(o@+2r^+#g94*u7tx7*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'oms.apps.OmsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'OMServer.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'OMServer.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default' : {
        # The django.db.backends.postgresql_psycopg2 backend has been renamed to django.db.backends.postgresql in Django 1.9
        'ENGINE' : 'django.db.backends.postgresql',
        'HOST' : '192.168.3.19',
        'PORT' : '5432',
        'NAME' : 'OMS',
        'USER' : 'postgres',
        'PASSWORD' : 'sco',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

# Custom User Auth model
AUTH_USER_MODEL = 'oms.OmsUser'

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
LOGIN_URL = reverse_lazy('oms:login')


STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

LOG_LEVEL= 'DEBUG' if DEBUG else 'INFO'

LOGGING = {
    'version' : 1,
    'disable_existing_loggers' : False,
    'formatters' : {
        'verbose' : {
            'format' : '%(asctime)s [%(levelname)s] %(name)s:%(lineno)d %(message)s',
            # 'format' : '%(asctime)s %(levelname)s %(module)s %(process)d %(thread)d %(message)s',
        },
        'simple' : {
            'format' : '%(levelname)s %(message)s'
        },
    },
    'handlers' : {
        'file' : {
            'level' : LOG_LEVEL,
            'class' : 'logging.FileHandler',
            'filename' : '/github/OMS/logs/debug.log',
            'formatter' : 'verbose',
        },
        'console' : {
            'level' : LOG_LEVEL,
            'class' : 'logging.StreamHandler',
            'formatter' : 'verbose',
        }
    },
    'loggers' : {
        'django.request' : {
            'handlers' : ['file'],
            'level' : LOG_LEVEL,
            'propagate' : True,
        },
        'oms' : {
            'handlers' : ['file', 'console'],
            'level' : LOG_LEVEL,
            'propagate' : True,
        },
    },
}