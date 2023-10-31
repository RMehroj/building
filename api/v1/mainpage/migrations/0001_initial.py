# Generated by Django 4.2.6 on 2023-10-31 12:41

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import location_field.models.plain
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=255)),
                ('license', models.ImageField(upload_to='static/static_dirs/images/license/')),
                ('achievements', models.ImageField(upload_to='static/static_dirs/images/achievements/')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'About',
            },
        ),
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('apartment', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10000)])),
                ('floor', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('parking', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1000)])),
                ('price', models.ImageField(upload_to='static/static_dirs/images/price/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Aparttment',
            },
        ),
        migrations.CreateModel(
            name='Newsroom',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='static/static_dirs/images/newsroom/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Newsroom',
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=512)),
                ('image', models.ImageField(upload_to='static/static_dirs/images/projects/')),
                ('description', models.TextField()),
                ('finish_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('aparttments', models.ManyToManyField(to='mainpage.apartment')),
            ],
            options={
                'db_table': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='SocialNetwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('instagram', models.URLField()),
                ('telegram', models.URLField()),
                ('facebook', models.URLField()),
            ],
            options={
                'db_table': 'SocialNetwork',
            },
        ),
        migrations.CreateModel(
            name='SalesOffice',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('city', models.CharField(max_length=255)),
                ('location', location_field.models.plain.PlainLocationField(max_length=63)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('projects', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainpage.projects')),
                ('social_network', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainpage.socialnetwork')),
            ],
            options={
                'db_table': 'SalesOffice',
            },
        ),
    ]
