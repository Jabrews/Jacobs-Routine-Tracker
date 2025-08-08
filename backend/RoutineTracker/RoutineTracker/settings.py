from pathlib import Path
import environ
import os

# --------------------------
# Base paths
# --------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
print('BASE DIR : ', BASE_DIR)
# --------------------------
# Env setup
# --------------------------
env = environ.Env()
# Reads backend/.env
environ.Env.read_env(BASE_DIR / '.env')

# --------------------------
# Core settings
# --------------------------
SECRET_KEY = env("DJANGO_SECRET_KEY")
DEBUG = env.bool("DJANGO_DEBUG")
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

# --------------------------
# Installed apps
# --------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # 3rd party
    "rest_framework",
    "corsheaders",

    # my apps
    "main",
]

# --------------------------
# Middleware
# --------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware", 
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "RoutineTracker.urls"

# --------------------------
# Templates (point to Vite dist for SPA if needed)
# --------------------------
FRONTEND_DIST = BASE_DIR.parent / "frontend" / "dist"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [FRONTEND_DIST] if FRONTEND_DIST.exists() else [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "RoutineTracker.wsgi.application"

# --------------------------
# Database (default sqlite, will read DATABASE_URL if set)
# --------------------------
# type: ignore
from typing import Any

if os.getenv("DATABASE_URL"):
    DATABASES = {"default": env.db("DATABASE_URL")}
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }


# --------------------------
# Password validation
# --------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# --------------------------
# Internationalization
# --------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# --------------------------
# Static files (Vite assets at /assets/)
# --------------------------
STATIC_URL = "/assets/"
STATICFILES_DIRS = [FRONTEND_DIST / "assets"] if (FRONTEND_DIST / "assets").exists() else []
STATIC_ROOT = BASE_DIR / "staticfiles"

# --------------------------
# Default primary key
# --------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# --------------------------
# CORS
# --------------------------
CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS", default=["http://localhost:5173"])
