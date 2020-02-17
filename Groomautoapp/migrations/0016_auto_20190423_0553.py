# Generated by Django 2.1.7 on 2019-04-23 00:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Groomautoapp', '0015_auto_20190413_1532'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='gmail',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='date',
            new_name='p_time',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='age',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='city',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='co_name',
        ),
        migrations.AddField(
            model_name='booking',
            name='s_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
