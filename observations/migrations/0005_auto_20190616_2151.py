# Generated by Django 2.2.2 on 2019-06-16 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('observations', '0004_auto_20190616_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obsrecords',
            name='setup',
            field=models.IntegerField(null=True),
        ),
    ]
