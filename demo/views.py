from django.shortcuts import render_to_response
from django.db.models import get_model, get_models
from civicdata import models as civicdata_models
from django.contrib.gis.maps.google.overlays import GPolygon


def browse(request):
    all_models = get_models(civicdata_models)
    all_models.sort()
    return render_to_response('browse.html', {'models': all_models})

def kml(request,object_name):
    model = get_model('civicdata', object_name)
    features = model.objects.all().collect()
    return render_to_response('base.kml', {'features': features } )

def dataset(request, object_name):
#    from django.contrib.gis.maps.google import GoogleZoom

#    gz = GoogleZoom()
    model = get_model('civicdata', object_name)
    fields = model._meta.fields
 #   features = model.objects.all().collect()
 #   centroid = features.centroid
    return render_to_response('dataset.html', {'model': model,
                                               'fields': fields, 
  #                                             'centroid': centroid,
#                                               'zoom': gz.get_zoom(features)
})
