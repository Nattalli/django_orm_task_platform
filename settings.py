import os
__import__("pysqlite3")
import sys  # noqa: E402

sys.modules["sqlite3"] = sys.modules.pop("pysqlite3")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = "KEEP_ME_SECRET_PLEASE"

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

USE_TZ = False

INSTALLED_APPS = ("db",)
