"""
Django settings for social_media_data_analyse_system project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import warnings
warnings.filterwarnings("ignore")
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%an6-gqv&n9v)*&h4988i-9$w5dxiv(^9w_f&y$cb7$fdw@)ua'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#ALLOWED_HOSTS = []
ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djcelery',
    'natural_disasters',
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

ROOT_URLCONF = 'social_media_data_analyse_system.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'social_media_data_analyse_system.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'social_media_database',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {'charset': 'utf8mb4'}
    },
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'collect_static')


#celery设置
from celery.schedules import crontab,timedelta
import djcelery
djcelery.setup_loader()
BROKER_URL = 'redis://127.0.0.1:6379/10'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/11'
CELERY_IMPORTS = ('natural_disasters.tasks')
CELERY_TIMEZONE = TIME_ZONE
#CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'

from celery.schedules import crontab
CELERYBEAT_SCHEDULE = {
    u'地震垃圾处理': {
        "task": "natural_disasters.tasks.earthquake_noise",
        "schedule": crontab(hour="3",minute="0"),
        "args": (),
    },
    u'台风垃圾处理': {
        "task": "natural_disasters.tasks.typhoon_noise",
        "schedule": crontab(hour="3",minute="0"),
        "args": (),
    },
    u'暴雨垃圾处理': {
        "task": "natural_disasters.tasks.rainstorm_noise",
        "schedule": crontab(hour="3",minute="0"),
        "args": (),
    },

    u'地震灾害损失分类': {
        "task": "natural_disasters.tasks.earthquake_category",
        "schedule": crontab(hour="3",minute="30"),
        "args": (),
    },
    u'台风灾害损失分类': {
        "task": "natural_disasters.tasks.typhoon_category",
        "schedule": crontab(hour="3",minute="30"),
        "args": (),
    },
    u'暴雨灾害损失分类': {
        "task": "natural_disasters.tasks.rainstorm_category",
        "schedule": crontab(hour="3",minute="30"),
        "args": (),
    },

    u'地震灾害信息提取': {
        "task": "natural_disasters.tasks.earthquake_event",
        "schedule": crontab(hour="3",minute="30"),
        "args": (),
    },
    u'台风灾害信息提取': {
        "task": "natural_disasters.tasks.typhoon_event",
        "schedule": crontab(hour="3",minute="30"),
        "args": (),
    },
    u'暴雨灾害信息提取': {
        "task": "natural_disasters.tasks.rainstorm_event",
        "schedule": crontab(hour="3",minute="30"),
        "args": (),
    },

    u'地震事件分类': {
        "task": "natural_disasters.tasks.earthquake_cluster",
        "schedule": crontab(hour="4",minute="0"),
        "args": (),
    },
    u'台风事件分类': {
        "task": "natural_disasters.tasks.typhoon_cluster",
        "schedule": crontab(hour="4",minute="0"),
        "args": (),
    },
    u'暴雨事件分类': {
        "task": "natural_disasters.tasks.rainstorm_cluster",
        "schedule": crontab(hour="4",minute="0"),
        "args": (),
    },
}