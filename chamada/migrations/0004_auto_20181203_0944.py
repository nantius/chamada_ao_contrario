# Generated by Django 2.1.3 on 2018-12-03 11:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chamada', '0003_auto_20181126_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamada',
            name='data',
            field=models.DateField(default=datetime.datetime(2018, 12, 3, 11, 44, 53, 645005, tzinfo=utc)),
        ),
    ]
