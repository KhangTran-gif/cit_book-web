# Generated by Django 5.0.6 on 2024-07-09 07:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('userid', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=35, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=100)),
                ('date_join', models.DateTimeField(default=datetime.datetime(2024, 7, 9, 14, 48, 21, 838702))),
                ('avatar', models.CharField(default='\\book_cit_web\\media\\imgUser\\', max_length=2000)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
