# Generated by Django 4.2.5 on 2024-02-21 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0028_remove_event_latitude_remove_event_longitude'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='status',
            field=models.CharField(choices=[('accepted', 'Accepted'), ('declined', 'Declined')], default='pending', max_length=10),
        ),
    ]