import sys
import os

for module in list(sys.modules):
    if "django." in module and "pytest" not in module:
        sys.modules.pop(module)

import django  # noqa: E402


sys.dont_write_bytecode = True
os.environ["DJANGO_SETTINGS_MODULE"] = "settings"
django.setup()
