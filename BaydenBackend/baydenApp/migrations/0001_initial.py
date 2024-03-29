# Generated by Django 5.0.2 on 2024-03-05 01:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('secondname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=20)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baydenApp.events')),
            ],
        ),
    ]
