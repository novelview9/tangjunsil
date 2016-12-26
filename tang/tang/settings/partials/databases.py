import os

import os

import dj_database_url

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

DATABASES = {}
DATABASES['default'] = dj_database_url.config(default=os.environ.get('DATABASE_URL'), )
