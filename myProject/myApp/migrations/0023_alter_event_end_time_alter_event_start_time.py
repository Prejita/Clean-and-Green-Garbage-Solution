# Generated by Django 4.2.5 on 2024-01-12 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0022_alter_event_end_time_alter_event_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.CharField(max_length=50, null='True'),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.CharField(max_length=50, null='True'),
        ),
    ]