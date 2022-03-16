"""Settings"""
from .settings import *

# Base
DEBUG = False
SECRET_KEY = "JJs1_#dto^kjlf=fdG5QbuHTGGM(*1_#dto^kjlf=fx&$+5l4khi!d)!-"
TEST_RUNNER = "django.test.runner.DiscoverRunner"

# Passwords
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]


# Cache
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": ""
    }
}
