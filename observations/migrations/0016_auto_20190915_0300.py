# Generated by Django 2.2.2 on 2019-09-15 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('observations', '0015_auto_20190722_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stars',
            name='hd_num',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stars',
            name='star_name',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
    ]
