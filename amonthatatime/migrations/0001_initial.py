# Generated by Django 3.1.6 on 2021-02-21 16:46

import amonthatatime.pythonsupport.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folder', models.CharField(choices=[('general', 'general')], max_length=20)),
                ('title', models.CharField(default='na', max_length=40)),
                ('photo', models.FileField(upload_to=amonthatatime.pythonsupport.models.folder_upload)),
                ('urls', models.TextField(default='na')),
            ],
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('subject', models.CharField(max_length=150)),
                ('contents', models.FileField(upload_to='htmls')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(default='2021')),
                ('month', models.CharField(choices=[('january', 'January'), ('february', 'February'), ('march', 'March'), ('april', 'April'), ('may', 'May'), ('june', 'June'), ('july', 'July'), ('august', 'August'), ('september', 'September'), ('october', 'October'), ('november', 'November'), ('december', 'December')], max_length=20)),
                ('month_number', models.IntegerField(default='1')),
                ('title', models.CharField(max_length=200)),
                ('whatsapp', models.TextField()),
                ('medley', models.TextField()),
                ('photo_columns', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=4)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
            ],
            options={
                'ordering': ['-created_on'],
                'unique_together': {('year', 'month')},
            },
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('conf_num', models.CharField(max_length=15)),
                ('confirmed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grams', models.FileField(upload_to=amonthatatime.pythonsupport.models.newletter_gram_path)),
                ('urls', models.TextField(default='na')),
                ('caption', models.TextField(default=0)),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='amonthatatime.post')),
            ],
        ),
    ]
