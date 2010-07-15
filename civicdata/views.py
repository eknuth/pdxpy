from django.shortcuts import render_to_response
from django.db.models import get_model, get_models
from civicdata import models as civicdata_models
import datetime

def index(request):
    return render_to_response('index.html', {})
