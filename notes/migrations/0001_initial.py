# Generated by Django 3.1.6 on 2021-03-16 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aphorism',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aphorism', models.TextField(blank=True, default=None, null=True)),
                ('author', models.CharField(blank=True, default=None, max_length=200)),
                ('notes', models.TextField(blank=True, default=None, null=True)),
            ],
        ),
    ]
