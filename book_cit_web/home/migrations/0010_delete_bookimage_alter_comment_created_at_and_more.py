# Generated by Django 5.0.7 on 2024-07-19 05:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_book_bookimage_alter_comment_created_at_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BookImage',
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 19, 12, 6, 52, 844665)),
        ),
        migrations.AlterField(
            model_name='favlist',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 19, 12, 6, 52, 844665)),
        ),
    ]
