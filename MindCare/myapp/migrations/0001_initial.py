# Generated by Django 5.1.2 on 2025-02-10 08:50

import django.db.models.deletion
import myapp.validators
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='Anonymous', max_length=50)),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='MentorshipApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field1', models.CharField(max_length=100)),
                ('field2', models.TextField()),
                ('field3', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Professional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('specialty', models.CharField(max_length=255)),
                ('contact_email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=15, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='professionals/')),
                ('available_slots', models.JSONField(default=list)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=10000)),
                ('video', models.FileField(upload_to='Video/', validators=[myapp.validators.file_size])),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('reason', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('professional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.professional')),
            ],
        ),
    ]
