from django.contrib.gis.db import models

class CivicModel(models.Model):
    class Meta:
        abstract = True

    @classmethod
    def model_name(self):
        return "%s" % self._meta.verbose_name
    @classmethod
    def object_name(self):
        return "%s" % self._meta.object_name.lower()




class Storefront_Improvement_Areas_pdx(CivicModel):
    geodb_oid = models.FloatField()
    objectid = models.FloatField()
    egh_public = models.FloatField()
    state_id = models.CharField(max_length=28)
    funding = models.CharField(max_length=19)
    storefront = models.CharField(max_length=33)
    active = models.CharField(max_length=12)
    shape_area = models.FloatField()
    shape_len = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()
    def __unicode__(self):
        return u'%s (%s)' % (self.storefront, self.state_id)

    class Meta:
        verbose_name = 'Storefront Improvement Area'

# Auto-generated `LayerMapping` dictionary for Storefront_Improvement_Areas_pdx model
storefront_improvement_areas_pdx_mapping = {
    'geodb_oid' : 'GEODB_OID',
    'objectid' : 'OBJECTID',
    'egh_public' : 'EGH_PUBLIC',
    'state_id' : 'STATE_ID',
    'funding' : 'FUNDING',
    'storefront' : 'STOREFRONT',
    'active' : 'ACTIVE',
    'shape_area' : 'SHAPE_AREA',
    'shape_len' : 'SHAPE_LEN',
    'geom' : 'MULTIPOLYGON',
}

class Bicycle_Network_pdx(CivicModel):
    geodb_oid = models.FloatField()
    objectid = models.FloatField()
    modifiedby = models.CharField(max_length=30)
    modifiedon = models.DateField()
    modifiedus = models.CharField(max_length=30)
    comments = models.CharField(max_length=254)
    tranplanid = models.CharField(max_length=15)
    segmentnam = models.CharField(max_length=50)
    status = models.CharField(max_length=15)
    facility = models.CharField(max_length=8)
    facilityde = models.CharField(max_length=50)
    projectid = models.CharField(max_length=15)
    yearbuilt = models.FloatField()
    num8inline = models.FloatField()
    material8i = models.CharField(max_length=3)
    num4inline = models.FloatField()
    material4i = models.CharField(max_length=3)
    assets_pdo = models.FloatField()
    shape_len = models.FloatField()
    geom = models.MultiLineStringField(srid=4326)
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'Bicycle Network'

# Auto-generated `LayerMapping` dictionary for Bicycle_Network_pdx model
bicycle_network_pdx_mapping = {
    'geodb_oid' : 'GEODB_OID',
    'objectid' : 'OBJECTID',
    'modifiedby' : 'MODIFIEDBY',
    'modifiedon' : 'MODIFIEDON',
    'modifiedus' : 'MODIFIEDUS',
    'comments' : 'COMMENTS',
    'tranplanid' : 'TRANPLANID',
    'segmentnam' : 'SEGMENTNAM',
    'status' : 'STATUS',
    'facility' : 'FACILITY',
    'facilityde' : 'FACILITYDE',
    'projectid' : 'PROJECTID',
    'yearbuilt' : 'YEARBUILT',
    'num8inline' : 'NUM8INLINE',
    'material8i' : 'MATERIAL8I',
    'num4inline' : 'NUM4INLINE',
    'material4i' : 'MATERIAL4I',
    'assets_pdo' : 'ASSETS_PDO',
    'shape_len' : 'SHAPE_LEN',
    'geom' : 'MULTILINESTRING',
}

class Bridges_pdx(CivicModel):
    assetid = models.CharField(max_length=15)
    locationid = models.CharField(max_length=15)
    imagepath = models.CharField(max_length=254)
    bridgetype = models.FloatField()
    bridgeidlo = models.CharField(max_length=15)
    bridgeidst = models.CharField(max_length=20)
    bridgeidfe = models.CharField(max_length=20)
    vehclearan = models.FloatField()
    materialma = models.CharField(max_length=50)
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()

    def __unicode__(self):
        return u'%s %s' % (self.bridgeidlo, self.assetid)

    class Meta:
        verbose_name = 'Bridge'

# Auto-generated `LayerMapping` dictionary for Bridges_pdx model
bridges_pdx_mapping = {
    'assetid' : 'ASSETID',
    'locationid' : 'LOCATIONID',
    'imagepath' : 'IMAGEPATH',
    'bridgetype' : 'BRIDGETYPE',
    'bridgeidlo' : 'BRIDGEIDLO',
    'bridgeidst' : 'BRIDGEIDST',
    'bridgeidfe' : 'BRIDGEIDFE',
    'vehclearan' : 'VEHCLEARAN',
    'materialma' : 'MATERIALMA',
    'geom' : 'MULTIPOLYGON',
}

class Leaf_Pickup_pdx(CivicModel):
    assets_pdo = models.CharField(max_length=14)
    route_pri_field = models.CharField(max_length=50)
    dist = models.CharField(max_length=10)
    milage = models.FloatField()
    geom = models.MultiLineStringField(srid=4326)
    objects = models.GeoManager()
    def __unicode__(self):
        return u'%s' % (self.route_pri_field)

    class Meta:
        verbose_name = 'Leaf Pickup'

# Auto-generated `LayerMapping` dictionary for Leaf_Pickup_pdx model
leaf_pickup_pdx_mapping = {
    'assets_pdo' : 'ASSETS_PDO',
    'route_pri_field' : 'ROUTE_PRI_',
    'dist' : 'DIST',
    'milage' : 'MILAGE',
    'geom' : 'MULTILINESTRING',
}

class Signage_Lighting_Imp_Prog_pdx(CivicModel):
    objectid = models.FloatField()
    state_id = models.CharField(max_length=20)
    siteaddr = models.CharField(max_length=37)
    sitecity = models.CharField(max_length=30)
    site_state = models.CharField(max_length=6)
    sitezip = models.CharField(max_length=8)
    elig_crite = models.CharField(max_length=120)
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()
    def __unicode__(self):
        return u'%s %s' % (self.elig_crite, self.siteaddr)

    class Meta:
        verbose_name = 'Signage Lighting Improvement Program'

# Auto-generated `LayerMapping` dictionary for Signage_Lighting_Imp_Prog_pdx model
signage_lighting_imp_prog_pdx_mapping = {
    'objectid' : 'OBJECTID',
    'state_id' : 'STATE_ID',
    'siteaddr' : 'SITEADDR',
    'sitecity' : 'SITECITY',
    'site_state' : 'SITE_STATE',
    'sitezip' : 'SITEZIP',
    'elig_crite' : 'ELIG_CRITE',
    'geom' : 'MULTIPOLYGON',
}

class LID_Streets_pdx(CivicModel):
    name = models.CharField(max_length=50)
    lid_status = models.CharField(max_length=50)
    projectid = models.FloatField()
    lid_commen = models.CharField(max_length=50)
    geom = models.MultiLineStringField(srid=4326)
    objects = models.GeoManager()
    def __unicode__(self):
        return u'%s' % (self.name)

    class Meta:
        verbose_name = 'LID Street'

# Auto-generated `LayerMapping` dictionary for LID_Streets_pdx model
lid_streets_pdx_mapping = {
    'name' : 'NAME',
    'lid_status' : 'LID_STATUS',
    'projectid' : 'PROJECTID',
    'lid_commen' : 'LID_COMMEN',
    'geom' : 'MULTILINESTRING',
}

class Parks_Taxlots_pdx(CivicModel):
    geodb_oid = models.FloatField()
    objectid = models.FloatField()
    camp_id = models.FloatField()
    rno = models.CharField(max_length=30)
    stateid = models.CharField(max_length=50)
    propertyid = models.CharField(max_length=25)
    geometry_s = models.CharField(max_length=75)
    camp_prope = models.FloatField()
    address = models.CharField(max_length=254)
    addition_s = models.CharField(max_length=254)
    year_acqui = models.FloatField()
    camp_sq_ft = models.FloatField()
    year_recor = models.FloatField()
    date_recor = models.DateField()
    grantor = models.CharField(max_length=50)
    acquisitio = models.CharField(max_length=250)
    ordinance = models.CharField(max_length=25)
    deed = models.CharField(max_length=25)
    notes = models.CharField(max_length=254)
    shape_area = models.FloatField()
    shape_len = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'Park Taxlot'

# Auto-generated `LayerMapping` dictionary for Parks_Taxlots_pdx model
parks_taxlots_pdx_mapping = {
    'geodb_oid' : 'GEODB_OID',
    'objectid' : 'OBJECTID',
    'camp_id' : 'CAMP_ID',
    'rno' : 'RNO',
    'stateid' : 'STATEID',
    'propertyid' : 'PROPERTYID',
    'geometry_s' : 'GEOMETRY_S',
    'camp_prope' : 'CAMP_PROPE',
    'address' : 'ADDRESS',
    'addition_s' : 'ADDITION_S',
    'year_acqui' : 'YEAR_ACQUI',
    'camp_sq_ft' : 'CAMP_SQ_FT',
    'year_recor' : 'YEAR_RECOR',
    'date_recor' : 'DATE_RECOR',
    'grantor' : 'GRANTOR',
    'acquisitio' : 'ACQUISITIO',
    'ordinance' : 'ORDINANCE',
    'deed' : 'DEED',
    'notes' : 'NOTES',
    'shape_area' : 'SHAPE_AREA',
    'shape_len' : 'SHAPE_LEN',
    'geom' : 'MULTIPOLYGON',
}

class Urban_Renewal_Area_pdx(CivicModel):
    geodb_oid = models.FloatField()
    objectid = models.FloatField()
    ura = models.CharField(max_length=30)
    egh_public = models.FloatField()
    acres = models.FloatField()
    shape_area = models.FloatField()
    shape_len = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()
    def __unicode__(self):
        return u'%s' % (self.ura)

    class Meta:
        verbose_name = 'Urban Renewal Area'

# Auto-generated `LayerMapping` dictionary for Urban_Renewal_Area_pdx model
urban_renewal_area_pdx_mapping = {
    'geodb_oid' : 'GEODB_OID',
    'objectid' : 'OBJECTID',
    'ura' : 'URA',
    'egh_public' : 'EGH_PUBLIC',
    'acres' : 'ACRES',
    'shape_area' : 'SHAPE_AREA',
    'shape_len' : 'SHAPE_LEN',
    'geom' : 'MULTIPOLYGON',
}

class Curbs_pdx(CivicModel):
    assetid = models.CharField(max_length=15)
    locationid = models.CharField(max_length=15)
    imagepath = models.CharField(max_length=254)
    curbtype = models.FloatField()
    width = models.FloatField()
    curbstyle_field = models.CharField(max_length=50)
    draintiles = models.CharField(max_length=50)
    histfeatur = models.CharField(max_length=50)
    geom = models.MultiLineStringField(srid=4326)
    objects = models.GeoManager()
    def __unicode__(self):
        return u'%s' % (self.assetid)

    class Meta:
        verbose_name = 'Curb'

# Auto-generated `LayerMapping` dictionary for Curbs_pdx model
curbs_pdx_mapping = {
    'assetid' : 'ASSETID',
    'locationid' : 'LOCATIONID',
    'imagepath' : 'IMAGEPATH',
    'curbtype' : 'CURBTYPE',
    'width' : 'WIDTH',
    'curbstyle_field' : 'CURBSTYLE_',
    'draintiles' : 'DRAINTILES',
    'histfeatur' : 'HISTFEATUR',
    'geom' : 'MULTILINESTRING',
}

class Parks_Easements_pdx(CivicModel):
    objectid = models.FloatField()
    property_n = models.CharField(max_length=55)
    property_i = models.FloatField()
    ordinance = models.FloatField()
    ordinance_field = models.FloatField()
    grant_type = models.CharField(max_length=25)
    easement_t = models.CharField(max_length=50)
    notes = models.CharField(max_length=254)
    acres = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()
    def __unicode__(self):
        return u'%s' % (self.property_n)

    class Meta:
        verbose_name = 'Parks Easement'

# Auto-generated `LayerMapping` dictionary for Parks_Easements_pdx model
parks_easements_pdx_mapping = {
    'objectid' : 'OBJECTID',
    'property_n' : 'PROPERTY_N',
    'property_i' : 'PROPERTY_I',
    'ordinance' : 'ORDINANCE',
    'ordinance_field' : 'ORDINANCE_',
    'grant_type' : 'GRANT_TYPE',
    'easement_t' : 'EASEMENT_T',
    'notes' : 'NOTES',
    'acres' : 'ACRES',
    'geom' : 'MULTIPOLYGON',
}

class Business_Associations(CivicModel):
    objectid = models.FloatField()
    perimeter = models.FloatField()
    busassc_field = models.FloatField()
    busassc_id = models.FloatField()
    name = models.CharField(max_length=70)
    apnba = models.CharField(max_length=8)
    contact = models.CharField(max_length=50)
    phone = models.CharField(max_length=35)
    email = models.CharField(max_length=70)
    shared = models.CharField(max_length=3)
    ba = models.CharField(max_length=20)
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()
    def __unicode__(self):
        return u'%s %s' % (self.ba, self.name)

    class Meta:
        verbose_name = 'Business Association'

# Auto-generated `LayerMapping` dictionary for Business_Associations model
business_associations_mapping = {
    'objectid' : 'OBJECTID',
    'perimeter' : 'PERIMETER',
    'busassc_field' : 'BUSASSC_',
    'busassc_id' : 'BUSASSC_ID',
    'name' : 'NAME',
    'apnba' : 'APNBA',
    'contact' : 'CONTACT',
    'phone' : 'PHONE',
    'email' : 'EMAIL',
    'shared' : 'SHARED',
    'ba' : 'BA',
    'geom' : 'MULTIPOLYGON',
}

class Curb_Ramps_pdx(CivicModel):
    nonassetid = models.CharField(max_length=15)
    imagepath = models.CharField(max_length=254)
    installdat = models.DateField()
    projectnum = models.CharField(max_length=10)
    adawarning = models.CharField(max_length=50)
    geom = models.MultiPointField(srid=4326)
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'Curb Ramp'

# Auto-generated `LayerMapping` dictionary for Curb_Ramps_pdx model
curb_ramps_pdx_mapping = {
    'nonassetid' : 'NONASSETID',
    'imagepath' : 'IMAGEPATH',
    'installdat' : 'INSTALLDAT',
    'projectnum' : 'PROJECTNUM',
    'adawarning' : 'ADAWARNING',
    'geom' : 'MULTIPOINT',
}

class Parks_Vegetation_Survey_pdx(CivicModel):
    geodb_oid = models.FloatField()
    objectid = models.FloatField()
    poly_code = models.CharField(max_length=10)
    acres = models.FloatField()
    property_c = models.CharField(max_length=10)
    wildlife_u = models.CharField(max_length=15)
    nvcs_class = models.CharField(max_length=254)
    nvcs_subcl = models.CharField(max_length=254)
    nvcs_group = models.CharField(max_length=254)
    nvcs_subgr = models.CharField(max_length=254)
    nvcs_forma = models.CharField(max_length=254)
    nvcs_ecolo = models.CharField(max_length=254)
    nvcs_allia = models.CharField(max_length=254)
    nvcs_assoc = models.CharField(max_length=254)
    survey_uni = models.CharField(max_length=254)
    past_land_field = models.CharField(max_length=254)
    last_visit = models.DateField()
    pct_tree_c = models.IntegerField()
    visit_note = models.CharField(max_length=254)
    visit_not2 = models.CharField(max_length=254)
    visit_not3 = models.CharField(max_length=254)
    wetland_no = models.CharField(max_length=254)
    visit_not4 = models.CharField(max_length=254)
    pct_non_na = models.IntegerField()
    ecological = models.CharField(max_length=25)
    shape_area = models.FloatField()
    shape_len = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'Parks Vegetation Survey'

# Auto-generated `LayerMapping` dictionary for Parks_Vegetation_Survey_pdx model
parks_vegetation_survey_pdx_mapping = {
    'geodb_oid' : 'GEODB_OID',
    'objectid' : 'OBJECTID',
    'poly_code' : 'POLY_CODE',
    'acres' : 'ACRES',
    'property_c' : 'PROPERTY_C',
    'wildlife_u' : 'WILDLIFE_U',
    'nvcs_class' : 'NVCS_CLASS',
    'nvcs_subcl' : 'NVCS_SUBCL',
    'nvcs_group' : 'NVCS_GROUP',
    'nvcs_subgr' : 'NVCS_SUBGR',
    'nvcs_forma' : 'NVCS_FORMA',
    'nvcs_ecolo' : 'NVCS_ECOLO',
    'nvcs_allia' : 'NVCS_ALLIA',
    'nvcs_assoc' : 'NVCS_ASSOC',
    'survey_uni' : 'SURVEY_UNI',
    'past_land_field' : 'PAST_LAND_',
    'last_visit' : 'LAST_VISIT',
    'pct_tree_c' : 'PCT_TREE_C',
    'visit_note' : 'VISIT_NOTE',
    'visit_not2' : 'VISIT_NOT2',
    'visit_not3' : 'VISIT_NOT3',
    'wetland_no' : 'WETLAND_NO',
    'visit_not4' : 'VISIT_NOT4',
    'pct_non_na' : 'PCT_NON_NA',
    'ecological' : 'ECOLOGICAL',
    'shape_area' : 'SHAPE_AREA',
    'shape_len' : 'SHAPE_LEN',
    'geom' : 'MULTIPOLYGON',
}

class Pavement_Maint_pdx(CivicModel):
    geodb_oid = models.FloatField()
    objectid = models.FloatField()
    modifiedby = models.CharField(max_length=30)
    modifiedon = models.DateField()
    modifiedus = models.CharField(max_length=30)
    comments = models.CharField(max_length=254)
    assetid = models.CharField(max_length=15)
    status = models.CharField(max_length=14)
    owner = models.CharField(max_length=15)
    maintresp = models.CharField(max_length=15)
    locationid = models.CharField(max_length=15)
    imagepath = models.CharField(max_length=254)
    sectionid = models.CharField(max_length=15)
    length = models.FloatField()
    townshipra = models.CharField(max_length=7)
    functional = models.CharField(max_length=8)
    jurisdicti = models.CharField(max_length=1)
    warranty = models.CharField(max_length=1)
    warrantyen = models.DateField()
    streetname = models.CharField(max_length=30)
    beglocatio = models.CharField(max_length=30)
    endlocatio = models.CharField(max_length=30)
    roadwidth = models.IntegerField()
    sqyards = models.FloatField()
    equiv28ft = models.FloatField()
    equiv12ft = models.FloatField()
    sealtype = models.CharField(max_length=8)
    pavetype = models.CharField(max_length=8)
    surfacetyp = models.CharField(max_length=8)
    surfacethi = models.IntegerField()
    basetype = models.CharField(max_length=8)
    basethickn = models.IntegerField()
    lastinspec = models.DateField()
    inspectedb = models.CharField(max_length=12)
    pci = models.IntegerField()
    numberofla = models.IntegerField()
    curb = models.CharField(max_length=1)
    coretaken = models.CharField(max_length=1)
    baserepair = models.CharField(max_length=1)
    maintenanc = models.CharField(max_length=12)
    maintenan2 = models.CharField(max_length=8)
    rehabdate = models.CharField(max_length=12)
    rehabtype = models.CharField(max_length=8)
    rehabthick = models.IntegerField()
    shape_len = models.FloatField()
    geom = models.MultiLineStringField(srid=4326)
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'Pavement Maint'

# Auto-generated `LayerMapping` dictionary for Pavement_Maint_pdx model
pavement_maint_pdx_mapping = {
    'geodb_oid' : 'GEODB_OID',
    'objectid' : 'OBJECTID',
    'modifiedby' : 'MODIFIEDBY',
    'modifiedon' : 'MODIFIEDON',
    'modifiedus' : 'MODIFIEDUS',
    'comments' : 'COMMENTS',
    'assetid' : 'ASSETID',
    'status' : 'STATUS',
    'owner' : 'OWNER',
    'maintresp' : 'MAINTRESP',
    'locationid' : 'LOCATIONID',
    'imagepath' : 'IMAGEPATH',
    'sectionid' : 'SECTIONID',
    'length' : 'LENGTH',
    'townshipra' : 'TOWNSHIPRA',
    'functional' : 'FUNCTIONAL',
    'jurisdicti' : 'JURISDICTI',
    'warranty' : 'WARRANTY',
    'warrantyen' : 'WARRANTYEN',
    'streetname' : 'STREETNAME',
    'beglocatio' : 'BEGLOCATIO',
    'endlocatio' : 'ENDLOCATIO',
    'roadwidth' : 'ROADWIDTH',
    'sqyards' : 'SQYARDS',
    'equiv28ft' : 'EQUIV28FT',
    'equiv12ft' : 'EQUIV12FT',
    'sealtype' : 'SEALTYPE',
    'pavetype' : 'PAVETYPE',
    'surfacetyp' : 'SURFACETYP',
    'surfacethi' : 'SURFACETHI',
    'basetype' : 'BASETYPE',
    'basethickn' : 'BASETHICKN',
    'lastinspec' : 'LASTINSPEC',
    'inspectedb' : 'INSPECTEDB',
    'pci' : 'PCI',
    'numberofla' : 'NUMBEROFLA',
    'curb' : 'CURB',
    'coretaken' : 'CORETAKEN',
    'baserepair' : 'BASEREPAIR',
    'maintenanc' : 'MAINTENANC',
    'maintenan2' : 'MAINTENAN2',
    'rehabdate' : 'REHABDATE',
    'rehabtype' : 'REHABTYPE',
    'rehabthick' : 'REHABTHICK',
    'shape_len' : 'SHAPE_LEN',
    'geom' : 'MULTILINESTRING',
}

class Zoning_Arrows_pdx(CivicModel):
    ltype = models.CharField(max_length=12)
    geom = models.MultiLineStringField(srid=4326)
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'Zoning Arrow'

# Auto-generated `LayerMapping` dictionary for Zoning_Arrows_pdx model
zoning_arrows_pdx_mapping = {
    'ltype' : 'LTYPE',
    'geom' : 'MULTILINESTRING',
}

class Zoning_Lines_pdx(CivicModel):
    cmp_id = models.FloatField()
    geom = models.MultiLineStringField(srid=4326)
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'Zoning Line'

# Auto-generated `LayerMapping` dictionary for Zoning_Lines_pdx model
zoning_lines_pdx_mapping = {
    'cmp_id' : 'CMP_ID',
    'geom' : 'MULTILINESTRING',
}

class Zoning_Anno_pdx(CivicModel):
    text = models.CharField(max_length=32)
    level = models.FloatField()
    symbol = models.FloatField()
    height = models.FloatField()
    geom = models.MultiLineStringField(srid=4326)
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'Zoning Anno'

# Auto-generated `LayerMapping` dictionary for Zoning_Anno_pdx model
zoning_anno_pdx_mapping = {
    'text' : 'TEXT',
    'level' : 'LEVEL',
    'symbol' : 'SYMBOL',
    'height' : 'HEIGHT',
    'geom' : 'MULTILINESTRING',
}

class Zoning_pdx(CivicModel):
    perimeter = models.FloatField()
    tmpzone = models.CharField(max_length=16)
    zone = models.CharField(max_length=14)
    cmp = models.CharField(max_length=6)
    ovrly = models.CharField(max_length=12)
    cmpovr = models.CharField(max_length=12)
    pldist = models.CharField(max_length=4)
    hist = models.CharField(max_length=2)
    consv = models.CharField(max_length=2)
    nrmp = models.CharField(max_length=2)
    update_field = models.DateField()
    uninc = models.CharField(max_length=1)
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'Zoning Area'


# Auto-generated `LayerMapping` dictionary for Zoning_pdx model
zoning_pdx_mapping = {
    'perimeter' : 'PERIMETER',
    'tmpzone' : 'TMPZONE',
    'zone' : 'ZONE',
    'cmp' : 'CMP',
    'ovrly' : 'OVRLY',
    'cmpovr' : 'CMPOVR',
    'pldist' : 'PLDIST',
    'hist' : 'HIST',
    'consv' : 'CONSV',
    'nrmp' : 'NRMP',
    'update_field' : 'UPDATE_',
    'uninc' : 'UNINC',
    'geom' : 'MULTIPOLYGON',
}

class Parks_pdx(CivicModel):
    geodb_oid = models.FloatField()
    objectid = models.FloatField()
    name = models.CharField(max_length=50)
    propertyid = models.FloatField()
    acres = models.FloatField()
    orient = models.CharField(max_length=29)
    shape_area = models.FloatField()
    shape_len = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'Park'

# Auto-generated `LayerMapping` dictionary for Parks_pdx model
parks_pdx_mapping = {
    'geodb_oid' : 'GEODB_OID',
    'objectid' : 'OBJECTID',
    'name' : 'NAME',
    'propertyid' : 'PROPERTYID',
    'acres' : 'ACRES',
    'orient' : 'ORIENT',
    'shape_area' : 'SHAPE_AREA',
    'shape_len' : 'SHAPE_LEN',
    'geom' : 'MULTIPOLYGON',
}

class Bicycle_Parking_pdx(CivicModel):
    assetid = models.CharField(max_length=15)
    locationid = models.CharField(max_length=15)
    imagepath = models.CharField(max_length=254)
    bikeparkty = models.FloatField()
    numspaces = models.IntegerField()
    numunits = models.IntegerField()
    bplevel = models.CharField(max_length=12)
    finish = models.CharField(max_length=20)
    mounting = models.CharField(max_length=25)
    rotation = models.FloatField()
    bpfund_field = models.CharField(max_length=50)
    bpstyle_field = models.CharField(max_length=50)
    covered_field = models.CharField(max_length=50)
    geom = models.MultiPointField(srid=4326)
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'Bicycle Parking Area'

# Auto-generated `LayerMapping` dictionary for Bicycle_Parking_pdx model
bicycle_parking_pdx_mapping = {
    'assetid' : 'ASSETID',
    'locationid' : 'LOCATIONID',
    'imagepath' : 'IMAGEPATH',
    'bikeparkty' : 'BIKEPARKTY',
    'numspaces' : 'NUMSPACES',
    'numunits' : 'NUMUNITS',
    'bplevel' : 'BPLEVEL',
    'finish' : 'FINISH',
    'mounting' : 'MOUNTING',
    'rotation' : 'ROTATION',
    'bpfund_field' : 'BPFUND_',
    'bpstyle_field' : 'BPSTYLE_',
    'covered_field' : 'COVERED_',
    'geom' : 'MULTIPOINT',
}

class Heritage_Trees_pdx(CivicModel):
    objectid = models.FloatField()
    treeid = models.FloatField()
    status = models.CharField(max_length=20)
    scientific = models.CharField(max_length=45)
    common_nam = models.CharField(max_length=30)
    stateid = models.CharField(max_length=20)
    address = models.CharField(max_length=31)
    height = models.IntegerField()
    spread = models.IntegerField()
    circumfere = models.FloatField()
    diameter = models.FloatField()
    year = models.IntegerField()
    owner = models.CharField(max_length=254)
    notes = models.CharField(max_length=254)
    geom = models.MultiPointField(srid=4326)
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'Heritage Tree'

# Auto-generated `LayerMapping` dictionary for Heritage_Trees_pdx model
heritage_trees_pdx_mapping = {
    'objectid' : 'OBJECTID',
    'treeid' : 'TREEID',
    'status' : 'STATUS',
    'scientific' : 'SCIENTIFIC',
    'common_nam' : 'COMMON_NAM',
    'stateid' : 'STATEID',
    'address' : 'ADDRESS',
    'height' : 'HEIGHT',
    'spread' : 'SPREAD',
    'circumfere' : 'CIRCUMFERE',
    'diameter' : 'DIAMETER',
    'year' : 'YEAR',
    'owner' : 'OWNER',
    'notes' : 'NOTES',
    'geom' : 'MULTIPOINT',
}

class Sidewalks_pdx(CivicModel):
    assetid = models.CharField(max_length=15)
    locationid = models.CharField(max_length=15)
    imagepath = models.CharField(max_length=254)
    drainagest = models.CharField(max_length=50)
    histfeatur = models.CharField(max_length=50)
    material_field = models.CharField(max_length=50)
    rampstyle_field = models.CharField(max_length=50)
    sidewalkty = models.CharField(max_length=50)
    warningsty = models.CharField(max_length=50)
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'Sidewalk'

# Auto-generated `LayerMapping` dictionary for Sidewalks_pdx model
sidewalks_pdx_mapping = {
    'assetid' : 'ASSETID',
    'locationid' : 'LOCATIONID',
    'imagepath' : 'IMAGEPATH',
    'drainagest' : 'DRAINAGEST',
    'histfeatur' : 'HISTFEATUR',
    'material_field' : 'MATERIAL_',
    'rampstyle_field' : 'RAMPSTYLE_',
    'sidewalkty' : 'SIDEWALKTY',
    'warningsty' : 'WARNINGSTY',
    'geom' : 'MULTIPOLYGON',
}

class Guardrails_pdx(CivicModel):
    assetid = models.CharField(max_length=15)
    locationid = models.CharField(max_length=15)
    imagepath = models.CharField(max_length=254)
    guardrailt = models.FloatField()
    totallengt = models.FloatField()
    sectionlen = models.FloatField()
    numbersect = models.FloatField()
    railheight = models.FloatField()
    numposts = models.FloatField()
    postspacin = models.CharField(max_length=15)
    postdimens = models.CharField(max_length=15)
    blockouts_field = models.CharField(max_length=50)
    farendtrea = models.CharField(max_length=50)
    nearendtre = models.CharField(max_length=50)
    posttype_field = models.CharField(max_length=50)
    railtype_field = models.CharField(max_length=50)
    geom = models.MultiLineStringField(srid=4326)
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'Guardrail'

# Auto-generated `LayerMapping` dictionary for Guardrails_pdx model
guardrails_pdx_mapping = {
    'assetid' : 'ASSETID',
    'locationid' : 'LOCATIONID',
    'imagepath' : 'IMAGEPATH',
    'guardrailt' : 'GUARDRAILT',
    'totallengt' : 'TOTALLENGT',
    'sectionlen' : 'SECTIONLEN',
    'numbersect' : 'NUMBERSECT',
    'railheight' : 'RAILHEIGHT',
    'numposts' : 'NUMPOSTS',
    'postspacin' : 'POSTSPACIN',
    'postdimens' : 'POSTDIMENS',
    'blockouts_field' : 'BLOCKOUTS_',
    'farendtrea' : 'FARENDTREA',
    'nearendtre' : 'NEARENDTRE',
    'posttype_field' : 'POSTTYPE_',
    'railtype_field' : 'RAILTYPE_',
    'geom' : 'MULTILINESTRING',
}

class LID_Boundaries_pdx(CivicModel):
    name = models.CharField(max_length=50)
    lid_status = models.CharField(max_length=50)
    projectid = models.FloatField()
    lid_commen = models.CharField(max_length=50)
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'LID Boundary'        
        verbose_name_plural = 'LID Boundaries'

# Auto-generated `LayerMapping` dictionary for LID_Boundaries_pdx model
lid_boundaries_pdx_mapping = {
    'name' : 'NAME',
    'lid_status' : 'LID_STATUS',
    'projectid' : 'PROJECTID',
    'lid_commen' : 'LID_COMMEN',
    'geom' : 'MULTIPOLYGON',
}

class TSP_Classifications_pdx(CivicModel):
    geodb_oid = models.FloatField()
    objectid = models.FloatField()
    modifiedby = models.CharField(max_length=30)
    modifiedon = models.DateField()
    modifiedus = models.CharField(max_length=30)
    comments = models.CharField(max_length=254)
    tranplanid = models.CharField(max_length=15)
    linkpath = models.CharField(max_length=254)
    streetname = models.CharField(max_length=50)
    traffic = models.CharField(max_length=8)
    transit = models.CharField(max_length=8)
    bicycle = models.CharField(max_length=8)
    pedestrian = models.CharField(max_length=8)
    freight = models.CharField(max_length=8)
    emergency = models.CharField(max_length=8)
    design = models.CharField(max_length=8)
    greenscape = models.CharField(max_length=3)
    shape_len = models.FloatField()
    geom = models.MultiLineStringField(srid=4326)
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'TSP Classification'

# Auto-generated `LayerMapping` dictionary for TSP_Classifications_pdx model
tsp_classifications_pdx_mapping = {
    'geodb_oid' : 'GEODB_OID',
    'objectid' : 'OBJECTID',
    'modifiedby' : 'MODIFIEDBY',
    'modifiedon' : 'MODIFIEDON',
    'modifiedus' : 'MODIFIEDUS',
    'comments' : 'COMMENTS',
    'tranplanid' : 'TRANPLANID',
    'linkpath' : 'LINKPATH',
    'streetname' : 'STREETNAME',
    'traffic' : 'TRAFFIC',
    'transit' : 'TRANSIT',
    'bicycle' : 'BICYCLE',
    'pedestrian' : 'PEDESTRIAN',
    'freight' : 'FREIGHT',
    'emergency' : 'EMERGENCY',
    'design' : 'DESIGN',
    'greenscape' : 'GREENSCAPE',
    'shape_len' : 'SHAPE_LEN',
    'geom' : 'MULTILINESTRING',
}

class Development_Opp_Areas_pdx(CivicModel):
    geodb_oid = models.FloatField()
    objectid = models.FloatField()
    egh_public = models.FloatField()
    state_id = models.CharField(max_length=20)
    name = models.CharField(max_length=75)
    shape_area = models.FloatField()
    shape_len = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'Development Opportunity Area'

# Auto-generated `LayerMapping` dictionary for Development_Opp_Areas_pdx model
development_opp_areas_pdx_mapping = {
    'geodb_oid' : 'GEODB_OID',
    'objectid' : 'OBJECTID',
    'egh_public' : 'EGH_PUBLIC',
    'state_id' : 'STATE_ID',
    'name' : 'NAME',
    'shape_area' : 'SHAPE_AREA',
    'shape_len' : 'SHAPE_LEN',
    'geom' : 'MULTIPOLYGON',
}

class Corner_Improved_pdx(CivicModel):
    assetid = models.CharField(max_length=15)
    locationid = models.CharField(max_length=15)
    imagepath = models.CharField(max_length=254)
    radius = models.FloatField()
    drainagest = models.CharField(max_length=50)
    extended_field = models.CharField(max_length=50)
    histfeatur = models.CharField(max_length=50)
    material_field = models.CharField(max_length=50)
    rampstyle_field = models.CharField(max_length=50)
    warningsty = models.CharField(max_length=50)
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'Improved Corner'

# Auto-generated `LayerMapping` dictionary for Corner_Improved_pdx model
corner_improved_pdx_mapping = {
    'assetid' : 'ASSETID',
    'locationid' : 'LOCATIONID',
    'imagepath' : 'IMAGEPATH',
    'radius' : 'RADIUS',
    'drainagest' : 'DRAINAGEST',
    'extended_field' : 'EXTENDED_',
    'histfeatur' : 'HISTFEATUR',
    'material_field' : 'MATERIAL_',
    'rampstyle_field' : 'RAMPSTYLE_',
    'warningsty' : 'WARNINGSTY',
    'geom' : 'MULTIPOLYGON',
}

class TSP_District_Boundaries_pdx(CivicModel):
    geodb_oid = models.FloatField()
    objectid = models.FloatField()
    tranplanid = models.CharField(max_length=15)
    districtna = models.CharField(max_length=50)
    cityname = models.CharField(max_length=30)
    shape_area = models.FloatField()
    shape_len = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'TSP District Boundary'
        verbose_name_plural = 'TSP District Boundaries'

# Auto-generated `LayerMapping` dictionary for TSP_District_Boundaries_pdx model
tsp_district_boundaries_pdx_mapping = {
    'geodb_oid' : 'GEODB_OID',
    'objectid' : 'OBJECTID',
    'tranplanid' : 'TRANPLANID',
    'districtna' : 'DISTRICTNA',
    'cityname' : 'CITYNAME',
    'shape_area' : 'SHAPE_AREA',
    'shape_len' : 'SHAPE_LEN',
    'geom' : 'MULTIPOLYGON',
}

class Parks_Desired_Fut_Cond_pdx(CivicModel):
    objectid = models.FloatField()
    propertyid = models.IntegerField()
    project = models.CharField(max_length=55)
    comment = models.CharField(max_length=50)
    acode = models.CharField(max_length=10)
    alliance = models.CharField(max_length=65)
    ecosystem = models.CharField(max_length=80)
    acres = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'Parks Desired Future Condition'

# Auto-generated `LayerMapping` dictionary for Parks_Desired_Fut_Cond_pdx model
parks_desired_fut_cond_pdx_mapping = {
    'objectid' : 'OBJECTID',
    'propertyid' : 'PROPERTYID',
    'project' : 'PROJECT',
    'comment' : 'COMMENT',
    'acode' : 'ACODE',
    'alliance' : 'ALLIANCE',
    'ecosystem' : 'ECOSYSTEM',
    'acres' : 'ACRES',
    'geom' : 'MULTIPOLYGON',
}

class Homebuyer_Opp_Area_pdx(CivicModel):
    geodb_oid = models.FloatField()
    objectid = models.FloatField()
    egh_public = models.FloatField()
    perimeter = models.FloatField()
    distress20 = models.FloatField()
    distress21 = models.FloatField()
    type = models.CharField(max_length=8)
    shape_area = models.FloatField()
    shape_len = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'Homebuyer Opportunity Area'

# Auto-generated `LayerMapping` dictionary for Homebuyer_Opp_Area_pdx model
homebuyer_opp_area_pdx_mapping = {
    'geodb_oid' : 'GEODB_OID',
    'objectid' : 'OBJECTID',
    'egh_public' : 'EGH_PUBLIC',
    'perimeter' : 'PERIMETER',
    'distress20' : 'DISTRESS20',
    'distress21' : 'DISTRESS21',
    'type' : 'TYPE',
    'shape_area' : 'SHAPE_AREA',
    'shape_len' : 'SHAPE_LEN',
    'geom' : 'MULTIPOLYGON',
}

class Transit_Stations_pdx(CivicModel):
    geodb_oid = models.FloatField()
    objectid = models.FloatField()
    tranplanid = models.CharField(max_length=15)
    transitsto = models.CharField(max_length=50)
    transitmod = models.CharField(max_length=30)
    status = models.CharField(max_length=15)
    geom = models.MultiPointField(srid=4326)
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'Transit Station'

# Auto-generated `LayerMapping` dictionary for Transit_Stations_pdx model
transit_stations_pdx_mapping = {
    'geodb_oid' : 'GEODB_OID',
    'objectid' : 'OBJECTID',
    'tranplanid' : 'TRANPLANID',
    'transitsto' : 'TRANSITSTO',
    'transitmod' : 'TRANSITMOD',
    'status' : 'STATUS',
    'geom' : 'MULTIPOINT',
}

class Pavement_Moratorium_pdx(CivicModel):
    geodb_oid = models.FloatField()
    objectid = models.FloatField()
    modifiedby = models.CharField(max_length=30)
    modifiedon = models.DateField()
    modifiedus = models.CharField(max_length=30)
    comments = models.CharField(max_length=254)
    nonassetid = models.CharField(max_length=15)
    status = models.CharField(max_length=14)
    owner = models.CharField(max_length=15)
    maintresp = models.CharField(max_length=15)
    imagepath = models.CharField(max_length=254)
    streetname = models.CharField(max_length=50)
    fromstreet = models.CharField(max_length=50)
    tostreet = models.CharField(max_length=50)
    datepaved = models.DateField()
    moratorium = models.DateField()
    proposedye = models.IntegerField()
    proposedse = models.CharField(max_length=10)
    projectnum = models.CharField(max_length=10)
    yearonly = models.IntegerField()
    projectown = models.CharField(max_length=12)
    shape_len = models.FloatField()
    geom = models.MultiLineStringField(srid=4326)
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'Pavement Moratorium'

# Auto-generated `LayerMapping` dictionary for Pavement_Moratorium_pdx model
pavement_moratorium_pdx_mapping = {
    'geodb_oid' : 'GEODB_OID',
    'objectid' : 'OBJECTID',
    'modifiedby' : 'MODIFIEDBY',
    'modifiedon' : 'MODIFIEDON',
    'modifiedus' : 'MODIFIEDUS',
    'comments' : 'COMMENTS',
    'nonassetid' : 'NONASSETID',
    'status' : 'STATUS',
    'owner' : 'OWNER',
    'maintresp' : 'MAINTRESP',
    'imagepath' : 'IMAGEPATH',
    'streetname' : 'STREETNAME',
    'fromstreet' : 'FROMSTREET',
    'tostreet' : 'TOSTREET',
    'datepaved' : 'DATEPAVED',
    'moratorium' : 'MORATORIUM',
    'proposedye' : 'PROPOSEDYE',
    'proposedse' : 'PROPOSEDSE',
    'projectnum' : 'PROJECTNUM',
    'yearonly' : 'YEARONLY',
    'projectown' : 'PROJECTOWN',
    'shape_len' : 'SHAPE_LEN',
    'geom' : 'MULTILINESTRING',
}

class ZipCodes_pdx(CivicModel):
    objectid = models.FloatField()
    zipcode = models.FloatField()
    name = models.CharField(max_length=25)
    type = models.CharField(max_length=25)
    state = models.CharField(max_length=2)
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'Zipcode'

# Auto-generated `LayerMapping` dictionary for ZipCodes_pdx model
zipcodes_pdx_mapping = {
    'objectid' : 'OBJECTID',
    'zipcode' : 'ZIPCODE',
    'name' : 'NAME',
    'type' : 'TYPE',
    'state' : 'STATE',
    'geom' : 'MULTIPOLYGON',
}

class Parks_Trails_pdx(CivicModel):
    geodb_oid = models.FloatField()
    objectid = models.FloatField()
    propertyid = models.FloatField()
    local_name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    status = models.CharField(max_length=25)
    manager = models.CharField(max_length=40)
    surface = models.CharField(max_length=50)
    width_ft = models.IntegerField()
    source = models.CharField(max_length=16)
    regional_t = models.CharField(max_length=20)
    columbia_s = models.CharField(max_length=35)
    forty_mile = models.CharField(max_length=35)
    i_205 = models.CharField(max_length=30)
    marine_dri = models.CharField(max_length=30)
    marquam = models.CharField(max_length=35)
    springwate = models.CharField(max_length=45)
    willamette = models.CharField(max_length=35)
    notes = models.CharField(max_length=45)
    red_electr = models.CharField(max_length=50)
    hillsdale_field = models.CharField(max_length=50)
    fanno_cree = models.CharField(max_length=60)
    miles = models.FloatField()
    shape_len = models.FloatField()
    geom = models.MultiLineStringField(srid=4326)
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'Parks Trail'

# Auto-generated `LayerMapping` dictionary for Parks_Trails_pdx model
parks_trails_pdx_mapping = {
    'geodb_oid' : 'GEODB_OID',
    'objectid' : 'OBJECTID',
    'propertyid' : 'PROPERTYID',
    'local_name' : 'LOCAL_NAME',
    'type' : 'TYPE',
    'status' : 'STATUS',
    'manager' : 'MANAGER',
    'surface' : 'SURFACE',
    'width_ft' : 'WIDTH_FT',
    'source' : 'SOURCE',
    'regional_t' : 'REGIONAL_T',
    'columbia_s' : 'COLUMBIA_S',
    'forty_mile' : 'FORTY_MILE',
    'i_205' : 'I_205',
    'marine_dri' : 'MARINE_DRI',
    'marquam' : 'MARQUAM',
    'springwate' : 'SPRINGWATE',
    'willamette' : 'WILLAMETTE',
    'notes' : 'NOTES',
    'red_electr' : 'RED_ELECTR',
    'hillsdale_field' : 'HILLSDALE_',
    'fanno_cree' : 'FANNO_CREE',
    'miles' : 'MILES',
    'shape_len' : 'SHAPE_LEN',
    'geom' : 'MULTILINESTRING',
}
