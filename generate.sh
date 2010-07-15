for i in `find raw -name *.shp`; do ogr2ogr -t_srs EPSG:4326 -a_srs EPSG:4326 -f "ESRI Shapefile" wgs84/`basename $i .shp` $i; done

for shpfile in `find civicdata/raw -name *.shp`; do python manage.py ogrinspect $shpfile `basename $shpfile .shp` --mapping --multi --srid=4326|tail -n +3; done >civicdata/models.py
