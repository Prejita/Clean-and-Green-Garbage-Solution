# Generated by Django 4.2.5 on 2024-01-01 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0007_dustbindata_delete_distancemeasurement'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dustbindata',
            old_name='fill_percentage',
            new_name='distance',
        ),
    ]