from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = False
if not DEBUG:
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


ALLOWED_HOSTS = ["127.0.0.1", os.getenv("ALLOWED_HOSTS")]


# Application definition

INSTALLED_APPS = [
    "daphne",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "trading",
    "channels",
    "uvicorn",
    "channels_redis",
]
ASGI_APPLICATION = "trading_system.asgi.application"

redis_url = os.getenv("REDIS_URL")
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [{"address": redis_url}],
        },
    },
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "trading_system.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "trading/templates")],  # Ensure this is correct
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

ASGI_APPLICATION = "trading_system.asgi.application"
WSGI_APPLICATION = "trading_system.wsgi.application"
# AUTH_USER_MODEL = 'trading.User'  # Replace with your actual app name


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "defaultdb",
        "USER": "avnadmin",
        "PASSWORD": "AVNS_oDL48ZDQK9C__oYZ6Y7",
        "HOST": "pg-2e467df3-akshatgarg715-d3e4.k.aivencloud.com",
        "PORT": "14026",
        "OPTIONS": {
            "sslmode": "require",
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = []


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/
LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
LOGIN_REDIRECT_URL = "home"

"""
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.example.com'  # Replace with your SMTP server
EMAIL_PORT = 587  # Common port for TLS
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@example.com'  # Replace with your email
EMAIL_HOST_PASSWORD = 'your_password'  # Replace with your password or app password
DEFAULT_FROM_EMAIL = 'Your Company <noreply@example.com>'"
"""

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
