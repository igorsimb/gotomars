"""
Production settings for project config.

This file overrides base.py and is used for the production environment.
"""

from .base import *  # noqa

DEBUG = env.bool("DJANGO_DEBUG", default=False)
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])
STATIC_ROOT = "/home/c99382/gotomars.na4u.ru/www/static"
MEDIA_ROOT = "/home/c99382/gotomars.na4u.ru/www/media"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": env("DBHOST"),
        "NAME": env("DBNAME"),
        "USER": env("DBUSER"),
        "PASSWORD": env("DBPASS"),
        "PORT": "5432",
    },
}

SECURE_HSTS_SECONDS = 60 * 60 * 24 * 365  # 1 year
SECURE_SSL_REDIRECT = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_PRELOAD = True
