# Generated by Django 2.2.2 on 2019-06-09 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('observations', '0002_auto_20190609_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obsfield',
            name='field_no',
            field=models.PositiveIntegerField(),
        ),
    ]
