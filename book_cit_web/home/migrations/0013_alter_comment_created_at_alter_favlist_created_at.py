# Generated by Django 5.0.7 on 2024-08-18 15:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_book_book_lang_alter_comment_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 18, 22, 1, 4, 931220)),
        ),
        migrations.AlterField(
            model_name='favlist',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 18, 22, 1, 4, 931220)),
        ),
    ]
