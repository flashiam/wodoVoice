# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class SpatialRefSys(models.Model):
    srid = models.IntegerField(primary_key=True)
    auth_name = models.CharField(max_length=256, blank=True, null=True)
    auth_srid = models.IntegerField(blank=True, null=True)
    srtext = models.CharField(max_length=2048, blank=True, null=True)
    proj4text = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spatial_ref_sys'


class WebsiteArticles(models.Model):
    artid = models.IntegerField(primary_key=True)
    updated_at = models.DateTimeField()
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    metatags = models.TextField(db_column='metaTags')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'website_articles'


class WodoAppuser(models.Model):
    userid = models.AutoField(db_column='userID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=200)
    contact = models.BigIntegerField(unique=True)
    profile = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=200)
    created_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wodo_appuser'


class WodoDutydenials(models.Model):
    denyid = models.IntegerField(db_column='denyID', primary_key=True)  # Field name made lowercase.
    updated_at = models.DateTimeField()
    reason = models.CharField(max_length=100, blank=True, null=True)
    transid = models.ForeignKey('WodoTransaction', models.DO_NOTHING)
    user = models.ForeignKey(WodoAppuser, models.DO_NOTHING)
    worker = models.ForeignKey('WodoWorkers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wodo_dutydenials'


class WodoFiltercache(models.Model):
    cacheid = models.IntegerField(db_column='CacheID', primary_key=True)  # Field name made lowercase.
    location = models.TextField(blank=True, null=True)
    wages = models.IntegerField()
    jobs = models.TextField()
    updated_at = models.DateTimeField()
    userf = models.ForeignKey(WodoAppuser, models.DO_NOTHING, db_column='userF_id')  # Field name made lowercase.
    add = models.TextField(blank=True, null=True)
    city = models.TextField()

    class Meta:
        managed = False
        db_table = 'wodo_filtercache'


class WodoHired(models.Model):
    hiredid = models.IntegerField(db_column='hiredID', primary_key=True)  # Field name made lowercase.
    updated_at = models.DateTimeField()
    orderid = models.ForeignKey('WodoTransaction', models.DO_NOTHING)
    userh = models.ForeignKey(WodoAppuser, models.DO_NOTHING, db_column='userH_id')  # Field name made lowercase.
    workeridh = models.ForeignKey('WodoWorkers', models.DO_NOTHING, db_column='workerIDH_id')  # Field name made lowercase.
    date = models.DateField()
    slot = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    extension = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wodo_hired'


class WodoReportworker(models.Model):
    reportid = models.IntegerField(db_column='reportID', primary_key=True)  # Field name made lowercase.
    reporttype = models.CharField(db_column='reportType', max_length=200)  # Field name made lowercase.
    description = models.TextField()
    actionneed = models.CharField(db_column='actionNeed', max_length=200)  # Field name made lowercase.
    status = models.CharField(max_length=100)
    updated_at = models.DateTimeField()
    userre = models.ForeignKey(WodoAppuser, models.DO_NOTHING, db_column='userRe_id')  # Field name made lowercase.
    workeridw = models.ForeignKey('WodoWorkers', models.DO_NOTHING, db_column='workerIDW_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wodo_reportworker'


class WodoSaved(models.Model):
    savedid = models.IntegerField(db_column='savedID', primary_key=True)  # Field name made lowercase.
    updated_at = models.DateTimeField()
    users = models.ForeignKey(WodoAppuser, models.DO_NOTHING, db_column='userS_id')  # Field name made lowercase.
    workerids = models.ForeignKey('WodoWorkers', models.DO_NOTHING, db_column='workerIDS_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wodo_saved'


class WodoTransaction(models.Model):
    amount = models.FloatField()
    orderid = models.CharField(db_column='orderID', unique=True, max_length=100)  # Field name made lowercase.
    transid = models.CharField(db_column='transID', unique=True, max_length=200)  # Field name made lowercase.
    transtype = models.CharField(db_column='transType', max_length=20)  # Field name made lowercase.
    purpose = models.CharField(max_length=30)
    timestamp = models.DateTimeField()
    usert = models.ForeignKey(WodoAppuser, models.DO_NOTHING, db_column='userT_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wodo_transaction'


class WodoWorkercalls(models.Model):
    callid = models.IntegerField(db_column='callID', primary_key=True)  # Field name made lowercase.
    date = models.DateField()
    updated_at = models.DateTimeField()
    callsid = models.CharField(db_column='callSid', max_length=100)  # Field name made lowercase.
    record = models.CharField(max_length=200, blank=True, null=True)
    transid = models.CharField(max_length=100)
    userid = models.ForeignKey(WodoAppuser, models.DO_NOTHING)
    workerid = models.ForeignKey('WodoWorkers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wodo_workercalls'


class WodoWorkers(models.Model):
    workerid = models.CharField(unique=True, max_length=20)
    agreeno = models.BigIntegerField(db_column='agreeNo', unique=True, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=200)
    img = models.CharField(max_length=500)
    skills = models.TextField(blank=True, null=True)
    exp = models.TextField(blank=True, null=True)
    datebirth = models.DateField(db_column='dateBirth')  # Field name made lowercase.
    lang = models.TextField(blank=True, null=True)
    wages = models.FloatField(blank=True, null=True)
    avgwork = models.FloatField(db_column='avgWork', blank=True, null=True)  # Field name made lowercase.
    distance = models.FloatField()
    offday = models.CharField(db_column='offDay', max_length=20)  # Field name made lowercase.
    idtype = models.CharField(db_column='idType', max_length=20)  # Field name made lowercase.
    idvalue = models.CharField(db_column='idValue', max_length=50)  # Field name made lowercase.
    active = models.BooleanField()
    gend = models.CharField(max_length=10)
    contact = models.BigIntegerField()
    strtime = models.TimeField()
    endtime = models.TimeField()
    add = models.TextField()
    city = models.CharField(max_length=100)
    coor = models.TextField()
    ageid = models.CharField(max_length=20)
    updated_at = models.DateTimeField()
    services = models.CharField(max_length=100, blank=True, null=True)
    wagestype = models.CharField(max_length=50, blank=True, null=True)
    verified = models.BooleanField(blank=True, null=True)
    service_tag = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wodo_workers'


class WodoWorkrating(models.Model):
    ratingid = models.IntegerField(db_column='ratingID', primary_key=True)  # Field name made lowercase.
    rat_1 = models.IntegerField(blank=True, null=True)
    rat_2 = models.IntegerField(blank=True, null=True)
    rat_3 = models.IntegerField(blank=True, null=True)
    rat_4 = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    hiredon = models.DateField(db_column='hiredOn')  # Field name made lowercase.
    updated_at = models.DateTimeField()
    userr = models.ForeignKey(WodoAppuser, models.DO_NOTHING, db_column='userR_id')  # Field name made lowercase.
    workeridr = models.ForeignKey(WodoWorkers, models.DO_NOTHING, db_column='workerIDR_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wodo_workrating'
