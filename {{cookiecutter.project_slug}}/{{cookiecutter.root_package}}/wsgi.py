import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ cookiecutter.root_package }}.settings")

application = get_wsgi_application()
