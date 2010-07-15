createdb civicdata
createlang plpgsql civicdata
psql civicdata -f /usr/share/postgresql/8.4/contrib/postgis.sql
psql civicdata -f /usr/share/postgresql/8.4/contrib/spatial_ref_sys.sql
psql civicdata -f civicdata/scripts/srid.sql
