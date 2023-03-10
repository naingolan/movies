"""
WSGI config for movies project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movies.settings")

application = get_wsgi_application()

# if name == "main":
# from django.core.management import execute_from_command_line
# execute_from_command_line(['manage.py', 'runserver', '0.0.0.0:{}'.format(PORT)])

