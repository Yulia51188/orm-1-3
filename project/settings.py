import os
from logging import DEBUG

from environs import Env

env = Env()
env.read_env()

#secretss
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
<<<<<<< Updated upstream
        "HOST": "checkpoint.devman.org",
        "PORT": "5434",
        "NAME": os.environ["NAME"],
        "USER":  os.environ["USER"],
        "PASSWORD":  os.environ["PASSWORD"],
=======
        "HOST": os.environ["DB_HOST"],
        "PORT": os.environ["DB_PORT"],
        "NAME": os.environ["DB_NAME"],
        "USER":  os.environ["DB_USER"],
        "PASSWORD":  os.environ["DB_PASSWORD"],
>>>>>>> Stashed changes
    }
}

INSTALLED_APPS = ["datacenter"]

SECRET_KEY = os.environ["SECRET_KEY"]
DEBUG =  os.environ["DEBUG"]

ROOT_URLCONF = "project.urls"

<<<<<<< Updated upstream

=======
ALLOWED_HOSTS= os.environ["ALLOWED_HOSTS"]
>>>>>>> Stashed changes

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
    },
]


USE_L10N = True

LANGUAGE_CODE = "ru-ru"

TIME_ZONE = "Europe/Moscow"

USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
