from django.db import models

# Models controlling BRITE Observations

class Satellite(models.Model):
#    sat_no = models.AutoField(primary_key=True)
    sat_id = models.CharField(max_length=5)
    sat_name = models.CharField(max_length=45)


class Status(models.Model):
    field_status = models.CharField(primary_key=True, max_length=45)


class ObsField(models.Model):
    field_no = models.PositiveIntegerField()
    field_name = models.CharField(unique=True, max_length=90)
    ra = models.DecimalField(max_digits=8, decimal_places=5)
    dec = models.DecimalField(max_digits=8, decimal_places=5)
    field_status = models.ForeignKey(Status, on_delete=models.CASCADE, db_column='field_status')

    def __str__(self):
        return str(self.field_no)+' - '+str(self.field_name)

    def field_num(self):
        return str(self.field_no)

class PrincInv(models.Model):
    first_name = models.CharField(max_length=90)
    last_name = models.CharField(max_length=90)
    initials = models.CharField(max_length=3)
    email = models.CharField(null=True, max_length=90)

class Stars(models.Model):
    hd_num = models.IntegerField(blank=True, null=True)
    v_mag = models.DecimalField(decimal_places=3, max_digits=5, blank=True, null=True)
    sp_type = models.CharField(max_length=45, blank=True, null=True)
    star_name = models.CharField(max_length=45, blank=True, null=True, unique=False)
    pi = models.ForeignKey(PrincInv, on_delete=models.CASCADE, null=True)
    availability = models.CharField(max_length=45, default='PP', blank=False, null=False)
    field = models.ForeignKey(ObsField, on_delete=models.CASCADE, null=True)

class ObsRecords(models.Model):
    idobs_records = models.AutoField(primary_key=True)
 #   hd_num = models.IntegerField(blank=False, null=True)
 #   v_mag = models.DecimalField(decimal_places=3, max_digits=5, blank=True, null=True)
 #   sp_type = models.CharField(max_length=45, blank=True, null=True)
 #   star_name = models.CharField(max_length=45, blank=True, null=True)
    sat = models.ForeignKey(Satellite, models.CASCADE, db_column='sat_id')
    setup = models.IntegerField(blank=False, null=True)
    obs_start = models.DecimalField(decimal_places=6, max_digits=13, blank=False, null=True)
    obs_end = models.DecimalField(decimal_places=6, max_digits=13, blank=False, null=True)
    nred = models.IntegerField(blank=False, null=True)
    norg = models.IntegerField(blank=False, null=True)
    exptime = models.IntegerField(blank=False, null=True)
    nstack = models.IntegerField(blank=False, null=True)
    xpos = models.IntegerField(blank=False, null=True)
    ypos = models.IntegerField(blank=False, null=True)
    xsize = models.IntegerField(blank=False, null=True)
    ysize = models.IntegerField(blank=False, null=True)
    obs_mode = models.CharField(max_length=10)
    availability = models.CharField(max_length=45, default='PP', blank=False, null=False)
    data_release = models.CharField(max_length=3, default='R5', blank=False, null=False)
#    field = models.ForeignKey(ObsField, on_delete=models.CASCADE, null=True)
    star = models.ForeignKey(Stars, on_delete=models.CASCADE, null=True)
#    field_no = models.ForeignKey(ObsField, models.CASCADE, db_column='field_no')
