from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
 
#DATABASES = {
#   'default': {
#        'ENGINE': 'sql_server.pyodbc',
#       'NAME': 'BDQUIZ',
#        'Trusted_Connection': 'yes',
#        'HOST': 'localhost',
#        'OPTIONS': {
#            'driver': 'SQL Server Native Client 11.0'
#        }
#    }
#}


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db2.sqlite3'),
    }
}