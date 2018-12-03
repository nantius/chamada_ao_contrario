from chamada_sovietica.settings.common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8j4$%1oiuxo2fsad*qweqwh812qw32132v5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}