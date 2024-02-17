import environ
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# get environment variables from '.env', in same folder that 'settings.py'
env = environ.Env()
environ.Env.read_env()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")


# Application definition

INSTALLED_APPS = [
    'accounts',
    'debug_toolbar',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework.authtoken',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = 'wrapper.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['wrapper/templates/',],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'wrapper.context_processors.base_data',
                'accounts.context_processors.base_data'
            ],
        },
    },
]

WSGI_APPLICATION = 'wrapper.wsgi.application'


# DATABASE
DATABASES = {
    'default': {
        'ENGINE': env("DATABASE_ENGINE"),
        'NAME': env("DATABASE_NAME"),
        'USER': env("DATABASE_USER"),
        'PASSWORD': env("DATABASE_PASSWORD"),
        'HOST': env("DATABASE_HOST"),
        'PORT': env("DATABASE_PORT"),
    }
}

# EMAILS (reset passwords, etc)
EMAIL_BACKEND = env('EMAIL_BACKEND')
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = env.int('EMAIL_PORT')
EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS")
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_TIMEOUT = env.int('EMAIL_TIMEOUT')
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')


# AUTHENTICATION

# Password validation
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

#If you have created a new authentication backend, uncomment the next lines and change the second element
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend', # This is the default that allows us to log in via username
    'accounts.authentication.EmailAuthBackend'
]

AUTH_USER_MODEL = 'accounts.User'
PASSWORD_RESET_TIMEOUT=1800  #In seconds


# INTERNATIONALIZATION
LANGUAGE_CODE = env('LANGUAGE_CODE')
TIME_ZONE = env('TIME_ZONE')
USE_I18N = env.bool("USE_I18N")
USE_TZ = env.bool("USE_TZ")


# FILES / STORAGE
# Static files (CSS, JavaScript, Images)
STATIC_URL = env('STATIC_URL')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]
STATIC_ROOT = env('STATIC_ROOT')

# Media files (Images, etc) Files uploaded by users
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = env('MEDIA_URL')


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# TEMPLATES
# If you use templates, uncomment the next lines and put the correct values for your app
# LOGIN_URL='/accounts/login/'
# LOGIN_REDIRECT_URL='/home'
# LOGOUT_REDIRECT_URL='/'
BASE_TEMPLATE_DIR='base/base.html'

# REST_FRAMEWORK SETTINGS
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

# REUSABLE_APP CUSTOM SETTINGS
#Custon settings (define here whatever variable needed by the reusable app)
SITE_DOMAIN_NAME = env('SITE_DOMAIN_NAME')