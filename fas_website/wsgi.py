# Файл для синхронных веб-серверов и приложений

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fas_website.settings')

application = get_wsgi_application()
