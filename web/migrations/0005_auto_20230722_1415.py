# Generated by Django 3.2.19 on 2023-07-22 09:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20230721_0342'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='responded',
            field=models.CharField(default='no', max_length=100),
        ),
        migrations.AlterField(
            model_name='analyticsdata',
            name='time',
            field=models.CharField(default=datetime.datetime(2023, 7, 22, 9, 15, 36, 792364, tzinfo=utc), max_length=100),
        ),
        migrations.AlterField(
            model_name='realtimedata',
            name='time',
            field=models.CharField(default=datetime.datetime(2023, 7, 22, 9, 15, 36, 947900, tzinfo=utc), max_length=100),
        ),
    ]