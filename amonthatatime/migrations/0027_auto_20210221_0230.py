# Generated by Django 3.1.6 on 2021-02-21 02:30

import amonthatatime.pythonsupport.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amonthatatime', '0026_image_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='photo',
            field=models.FileField(upload_to=amonthatatime.pythonsupport.models.folder_upload),
        ),
    ]
