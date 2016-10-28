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
    'dal',
    'dal_select2',
    'grappelli',
    'filebrowser',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.gis',
    'haystack',
    'map',
    'whitechapel_pages',
    'whitechapel_users',
    'whitechapel_blog',
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
    'analytical',
    # django-allauth and login providers
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # django-allauth login providers
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    # Honey pot app to stop bad spammers that are bad
    'honeypot',
    # Celery email message queue
    'djcelery_email',
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
    #'honeypot.middleware.HoneypotMiddleware',
)

ROOT_URLCONF = 'whitechapel.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
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
                'whitechapel_pages.context_processors.allow_indexing',
                'map.context_processors.last_feature',
                'map.context_processors.next_edit',
                'whitechapel_blog.context_processors.blog_category_links',
                'whitechapel_blog.context_processors.blog_post_list',
                'whitechapel_blog.context_processors.latest_contributions',
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

STATIC_ROOT = BASE_DIR.child('static')

#STATICFILES_DIRS = [
#    BASE_DIR.child('static'),
#    'static/',
#]

# Media Settings

MEDIA_ROOT = BASE_DIR.child('media')
MEDIA_URL = '/media/'


# Logging

LOG_DIR = BASE_DIR.child('logs')

# Emails 

EMAIL_SUBJECT_PREFIX = 'Survey of London Whitechapel | '

# Image file size limits. Restricts uploaded files to images with a maximum size of 2.5MB

CONTENT_TYPES = ['image']

MAX_UPLOAD_SIZE = 2621440

### App-Specific Settings ###

# Django-ckeditor Settings

CKEDITOR_UPLOAD_PATH = 'uploads/'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Format', 'Bold', 'Italic', 'Underline'],
            ['BulletedList', 'Blockquote'],
            ['Link', 'Unlink', 'Anchor'],
            ['Image', 'Flash', 'Table', 'HorizontalRule', 'SpecialChar'],
            ['RemoveFormat', 'Source']
        ]
    },
}

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
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://127.0.0.1:8080/solr',
    },
}

HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

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

LOGIN_REDIRECT_URL = 'map_home'

ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_EMAIL_VERIFICATION = 'none'

ACCOUNT_AUTHENTICATION_METHOD = 'username_email'

SOCIALACCOUNT_PROVIDERS = { 
    'google':
        { 'SCOPE': ['profile', 'email'],
          'AUTH_PARAMS': { 'access_type': 'online' } 
        }
    }

ACCOUNT_FORMS = {
    'signup': 'whitechapel_users.forms.WhitechapelSignupForm',
}

# django-honeypot 

HONEYPOT_FIELD_NAME = 'phone_number'