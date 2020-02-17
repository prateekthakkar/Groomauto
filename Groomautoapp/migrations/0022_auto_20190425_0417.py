# Generated by Django 2.1.7 on 2019-04-24 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Groomautoapp', '0021_auto_20190425_0402'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='u_detail',
            name='mail_id',
        ),
        migrations.RemoveField(
            model_name='u_detail',
            name='password',
        ),
        migrations.AddField(
            model_name='u_detail',
            name='address',
            field=models.CharField(default='Ahm', max_length=50),
        ),
        migrations.AddField(
            model_name='u_detail',
            name='area',
            field=models.CharField(default='Ghatlodiya', max_length=30),
        ),
        migrations.AddField(
            model_name='u_detail',
            name='pincode',
            field=models.CharField(default='380061', max_length=6),
        ),
        migrations.AlterField(
            model_name='u_detail',
            name='u_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
