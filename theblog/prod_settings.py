from .settings import * 
import dj_database_url

DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['henock.herokuapp.com']

MIDDLEWARE = [

	'whitenoise.middleware.WhiteNoiseMiddleware',

]

DATABASES['default'] = dj_database_url.config()

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'