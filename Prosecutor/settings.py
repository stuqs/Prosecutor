"""
Django settings for Prosecutor project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# BASE_DIR = '/home/webadmin/public_html/telephone.com/'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4iz&6caoy&&8kj&-mlgi(vf)^&-w=7^shp5^ap%czamjo$0a@x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# True
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['10.10.50.100',
                 'telephone.com',
                 'www.telephone.com',
                 '127.0.0.1']


# Application definition

INSTALLED_APPS = (
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Telephone',
    'django_cleanup',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'Prosecutor.urls'

WSGI_APPLICATION = 'Prosecutor.wsgi.application'

# CREATE DATABASE `Prosecutor` CHARACTER SET utf8 COLLATE utf8_general_ci;

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'prosecutor',
        'USER': 'prosecutor',
        'PASSWORD': 'ntktajyysqcghfdjxybr',
        'HOST': '10.10.50.154',
        'OPTIONS': {
            'autocommit': True,
            }
        }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/media/'
STATIC_ROOT = '/media/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "media"),
    )

MEDIA_ROOT = BASE_DIR
# MEDIA_ROOT = '/home/webadmin/public_html/telephone.com/'
MEDIA_URL = '/photo/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
)

ADMIN_TOOLS_INDEX_DASHBOARD = 'Prosecutor.dashboard.CustomIndexDashboard'
ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'Prosecutor.dashboard.CustomAppIndexDashboard'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
)