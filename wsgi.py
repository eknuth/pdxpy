#!/usr/bin/env python

import os
import sys

apache_configuration= os.path.dirname(__file__)
project = os.path.dirname(apache_configuration)
workspace = os.path.dirname(project)
sys.path.append(workspace) 
sys.path.append('/opt/pdxpy')

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
os.environ['PYTHON_EGG_CACHE'] = '/opt/pdxpy/eggs'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
