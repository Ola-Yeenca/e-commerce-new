import os
from django.core.wsgi import get_wsgi_application
import sys

print(sys.path)



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shopware.settings')

application = get_wsgi_application()
