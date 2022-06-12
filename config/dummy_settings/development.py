'''
Its Imports the settings from the base settings file
'''
from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-yt#=h%x9(qak@x#4==0uap-=w!w22^($=x-1m-#(%ft+(%p7*h'

ALLOWED_HOSTS = ['*']

# * Database
# ? https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# * Static files (CSS, JavaScript, Images)
# ? https://docs.djangoproject.com/en/4.0/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

# Simplified static file serving.
# ? https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
