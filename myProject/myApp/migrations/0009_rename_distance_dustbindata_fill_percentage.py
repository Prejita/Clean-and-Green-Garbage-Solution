# Generated by Django 4.2.5 on 2024-01-04 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0008_rename_fill_percentage_dustbindata_distance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dustbindata',
            old_name='distance',
            new_name='fill_percentage',
        ),
    ]
