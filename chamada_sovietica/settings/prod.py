from chamada_sovietica.settings.common import *
import dj_database_url
import django_heroku

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

django_heroku.settings(locals())

DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)



