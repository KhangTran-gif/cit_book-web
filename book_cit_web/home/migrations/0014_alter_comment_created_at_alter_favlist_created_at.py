# Generated by Django 5.0.6 on 2024-08-24 04:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_comment_created_at_alter_favlist_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 24, 11, 11, 8, 473020)),
        ),
        migrations.AlterField(
            model_name='favlist',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 24, 11, 11, 8, 473020)),
        ),
    ]
