# Generated by Django 3.1.6 on 2021-02-20 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amonthatatime', '0019_postimage_grams'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.FileField(upload_to='')),
            ],
        ),
    ]
