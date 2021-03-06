from os.path import join, abspath, dirname
from secret import *

ADMINS = (
    ('Philippe Guay', 'guay.philippe@gmail.com'),
)

MANAGERS = ADMINS
SITE_ID = 1

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Montreal'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html

LANGUAGE_CODE = 'fr-CA'
gettext = lambda s: s
LANGUAGES = (
    ('fr', gettext('French')),
    ('en', gettext('English'))
)

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True


# =================================================
#  PATHS CONFIGURATION
# =================================================
here = lambda *x: join(abspath(dirname(__file__)), *x)

# ROOT
PROJECT_ROOT = here('..','..')
root = lambda *x: join(abspath(PROJECT_ROOT), *x)

# MEDIA
MEDIA_URL = '/media/'
MEDIA_ROOT = root('media')

# STATIC
STATIC_URL = '/static/'
STATIC_ROOT  = root('static')

# STATICFILES_DIRS = (
#     root('static'),
# )

# TEMPLATES
TEMPLATE_DIRS = (
    root('templates'),
)

# LOCALE
LOCALE_PATHS = (
    root('../locale'),
    root('static/js'),
)

# =================================================
#  PACKAGES CONFIGS
# =================================================
LESS_MTIME_DELAY = 2
LESS_USE_CACHE = False

STATIC_PRECOMPILER_COMPILERS=(
  # "static_precompiler.compilers.CoffeeScript",
  # "static_precompiler.compilers.SASS",
  # "static_precompiler.compilers.SCSS",
  "static_precompiler.compilers.LESS",
)

CRISPY_TEMPLATE_PACK = 'bootstrap3'


MODELTRANSLATION_TRANSLATION_FILES = (
    'corewine.translation',
)

# =================================================
#  CONTEXT PROCESSORS
# =================================================

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',

)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'less.finders.LessFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'static_precompiler.finders.StaticPrecompilerFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.contrib.admindocs.middleware.XViewMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'project.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'project.wsgi.application'


# ADMIN_FOR = ('project.corewine','project.core','project.blog')
# =================================================
#  INSTALLED APPS
# =================================================

INSTALLED_APPS = (
    'django.contrib.admindocs',
    'django.contrib.admin',
    'django.contrib.auth',
    'blog',
    'braces',
    'django.contrib.contenttypes',
    'corewine',
    'crispy_forms',
    'django.contrib.formtools',
    'django.contrib.humanize',
    'static_precompiler',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'rest_framework',
    'south',
    'core',
    'taggit',
    'django.contrib.staticfiles',
    'modeltranslation',
)


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'DEBUG',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}