from .base import * #noqa

DEBUG = True
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
SECRET_KEY = os.getenv("SECRET_KEY", "dont_use_this_default_key_ever")

# Development-specific apps and middlewares
INSTALLED_APPS += [
    "debug_toolbar",
    ]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    ]

# Email backend for development
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend:"

# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://127.0.0.1:6379/1",
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#         },
#     }
# }

INTERNAL_IPS = ("127.0.0.1",)