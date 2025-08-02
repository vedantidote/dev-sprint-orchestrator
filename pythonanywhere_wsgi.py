# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
import os
import sys

# Add your project directory to the sys.path
path = '/home/yourusername/dev-sprint-orchestrator'
if path not in sys.path:
    sys.path.append(path)

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'devsprintorchestrator.settings_production'

# Serve Django via WSGI
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application() 