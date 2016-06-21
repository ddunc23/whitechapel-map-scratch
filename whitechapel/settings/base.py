"""
Django settings for whitechapel project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from unipath import Path

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BASE_DIR = Path(__file__).ancestor(3)

# Application definition

INSTALLED_APPS = (
    'grappelli',
    'filebrowser',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'haystack',
    'map',
    'whitechapel_pages',
    'whitechapel_users',
    'djgeojson',
    'leaflet',
    'ckeditor',
    'ckeditor_uploader',
    'rest_framework',
    'rest_framework_gis',
    'taggit',
    'crispy_forms',
    'easy_thumbnails',
    'embed_video',
    # django-allauth and login providers
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # django-allauth login providers
    #'allauth.socialaccount.providers.facebook',
    #'allauth.socialaccount.providers.twitter',
    #'allauth.socialaccount.providers.google',
    #'allauth.socialaccount.providers.pinterest',
    #'allauth.socialaccount.providers.instagram',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'whitechapel.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [os.path.join(BASE_DIR, 'templates/')],
        'DIRS': (BASE_DIR.child('templates'),),
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'whitechapel_pages.context_processors.menu_links',
                'whitechapel_pages.context_processors.category_links',
                'map.context_processors.last_feature',
            ],
        },
    },
]

WSGI_APPLICATION = 'whitechapel.wsgi.application'


# Database - moved to 'secret_settings.py'
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# Database connection settings are stored untracked in secret_settings.py

# Caching

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'TIMEOUT': 0,
    }
}


# Serializers

SERIALIZATION_MODULES = {
    'geojson': 'djgeojson.serializers'
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

# STATIC_ROOT = BASE_DIR.child('static')

STATICFILES_DIRS = [
    BASE_DIR.child('static'),
    'static/',
]

# Media Settings

MEDIA_ROOT = BASE_DIR.child('media')
MEDIA_URL = '/media/'


# Logging

LOG_DIR = BASE_DIR.child('logs')

# Emails 

EMAIL_SUBJECT_PREFIX = 'Survey of London Whitechapel | '


### App-Specific Settings ###

# Django-ckeditor Settings

CKEDITOR_UPLOAD_PATH = 'uploads/'

# Django-leaflet Settings

LEAFLET_CONFIG = {
    'TILES': 'https://{s}.surveyoflondon.org/tileserver.php?/index.json?/whitechapel_building_footprints_with_open_spaces/{z}/{x}/{y}.png',
    'DEFAULT_CENTER': (51.5161, -0.067),
    'DEFAULT_ZOOM': 16,
}

# Django-rest-framework Settings

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

# Haystack Settings

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    },
}

# Grapelli

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.request",
)

GRAPPELLI_ADMIN_TITLE = 'Survey of London Whitechapel'

# django-filebrowser

FILEBROWSER_DIRECTORY = 'uploads/'

# Crispy Forms

CRISPY_TEMPLATE_PACK = 'bootstrap3'

# django-allauth

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

SITE_ID = 1

LOGIN_REDIRECT_URL = '/map/'

ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
