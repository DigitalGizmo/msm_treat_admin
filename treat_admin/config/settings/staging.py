"""
Server Django settings.
"""
from .base import *

ALLOWED_HOSTS = ['msm-treat-admin.digitalgizmo.com', 'temp-treat-admin.digitalgizmo.com', '127.0.0.1']


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Just in case I need different db settings
