# Generated by Django 4.2.5 on 2024-01-04 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0009_rename_distance_dustbindata_fill_percentage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dustbindata',
            old_name='fill_percentage',
            new_name='distance',
        ),
        migrations.RemoveField(
            model_name='dustbindata',
            name='is_filled',
        ),
        migrations.AddField(
            model_name='dustbindata',
            name='status',
            field=models.CharField(default='Pending', max_length=10),
        ),
    ]
