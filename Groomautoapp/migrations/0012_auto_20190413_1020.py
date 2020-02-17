# Generated by Django 2.0 on 2019-04-13 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Groomautoapp', '0011_auto_20190401_1036'),
    ]

    operations = [
        migrations.RenameField(
            model_name='combo',
            old_name='c_name',
            new_name='co_name',
        ),
        migrations.AddField(
            model_name='booking',
            name='co_name',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.PROTECT, to='Groomautoapp.combo'),
            preserve_default=False,
        ),
    ]
