# Generated by Django 2.1.7 on 2019-04-23 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Groomautoapp', '0017_auto_20190424_0346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='c_name',
            field=models.CharField(max_length=40, primary_key=True, serialize=False),
        ),
    ]
