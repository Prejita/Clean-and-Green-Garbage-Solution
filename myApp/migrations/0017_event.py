# Generated by Django 4.2.5 on 2024-01-11 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0016_notification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('organizer', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('location', models.CharField(max_length=255)),
                ('category', models.CharField(choices=[('Conference', 'Conference'), ('Seminar', 'Seminar'), ('Workshop', 'Workshop'), ('Clean-up Campaigns', 'Clean-up Campaigns'), ('Tree-planting Drives', 'Tree-planting Drives'), ('Others', 'Others')], max_length=20)),
                ('description', models.TextField()),
            ],
        ),
    ]
