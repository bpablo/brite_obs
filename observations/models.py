from django.db import models

# Models controlling BRITE Observations

class Satellite(models.Model):
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
        return self.field_name


class ObsRecords(models.Model):
    idobs_records = models.AutoField(primary_key=True)
    star_id = models.CharField(max_length=45)
    star_name = models.CharField(max_length=45, blank=True, null=True)
    sp_type = models.CharField(max_length=45, blank=True, null=True)
    obs_start = models.CharField(max_length=45)
    obs_end = models.CharField(max_length=45)
    sat = models.ForeignKey('Satellite', models.CASCADE)
    no_obs = models.IntegerField()
    obs_mode = models.CharField(max_length=10)
    availability = models.CharField(max_length=45)
    field_no = models.ForeignKey(ObsField, models.CASCADE, db_column='field_no')
    setup = models.IntegerField(null=False)