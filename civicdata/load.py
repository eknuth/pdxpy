import os, glob
from django.contrib.gis.utils import LayerMapping
from django.db.models import get_models, get_model

import models as civicdata_models

source={}
mapping={}
for name in glob.glob('civicdata/wgs84/*/*.shp'):
    model_name = os.path.basename(name)[0:-4]
    source[model_name]=name
    mapping[model_name]=eval('civicdata_models.%s_mapping' % model_name.lower())

def run(verbose=True):         
    for m in get_models(civicdata_models):
        model_name = m._meta.object_name


        try:
            lm = LayerMapping(m, source[model_name], mapping[model_name], 
                              transform=False, encoding='iso-8859-1')
            lm.save(strict=True, verbose=verbose)
            print "Saved %s" % model_name
        except:
            print "Couldn't finish %s" %model_name
    #for m in get_models(civicdata_models):
    #    model_name =
    #    shpfile = 'civicdata/raw/%s.shp' % model_name
    #    print "%s, %s" % (model_name, shpfile)


