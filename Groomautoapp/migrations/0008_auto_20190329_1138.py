# Generated by Django 2.1.7 on 2019-03-29 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Groomautoapp', '0007_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='u_login',
            fields=[
                ('u_id', models.CharField(max_length=3)),
                ('mail_id', models.EmailField(max_length=15, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=15)),
            ],
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='email',
            new_name='mail_id',
        ),
    ]
