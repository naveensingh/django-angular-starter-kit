# SECURITY WARNING: don't run with debug turned on in production!
from settings.config import Config

CONFIG = Config()


DEBUG = True
ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# =============================================================================
# DATABASE SETTINGS
# =============================================================================
mysql_config = CONFIG.mysql_config()
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.mysql',
        'NAME': mysql_config["database_name"],
        'USER': mysql_config["database_user"],
        'PASSWORD': mysql_config["database_user_password"],
        'HOST': '127.0.0.1',
        'PORT': '33060',
    }
}

