from django.conf.urls.defaults import *
from django.contrib.gis import admin
from django.conf import settings
from civicdata import views
from demo import views as demo_views

admin.autodiscover()

urlpatterns = patterns('',
                       (r'^admin/', include(admin.site.urls)),

                       (r'^browse', demo_views.browse),
#                       (r'^dataset/(?P<object_name>.*).kml$', demo_views.kml),
                       (r'^dataset/(?P<object_name>.*)$', demo_views.dataset),

                       (r'^static/(?P<path>.*)$', 'django.views.static.serve',
                        {'document_root': settings.STATIC_DOC_ROOT}),
                       (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                        {'document_root': settings.STATIC_DOC_ROOT}),
                       (r'^', views.index),
)
