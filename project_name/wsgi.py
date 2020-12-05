"""
WSGI config.
"""

import os

from django.core.wsgi import get_wsgi_application

from . import load_env

load_env.load_env()
if 'DATABASE_URL' in os.environ:
    # Dokku or similar
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings.deploy")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings")

application = get_wsgi_application()

try:
    from whitenoise.django import DjangoWhiteNoise
except ImportError:
    pass
else:
    application = DjangoWhiteNoise(application)
