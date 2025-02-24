"""
Production settings for project config.

This file overrides base.py and is used for the production environment.
"""

from .base import *  # noqa

DEBUG = env.bool("DJANGO_DEBUG", default=False)
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])
