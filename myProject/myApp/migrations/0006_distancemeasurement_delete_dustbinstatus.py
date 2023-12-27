# Generated by Django 4.2.5 on 2023-12-27 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0005_dustbinstatus_delete_dustbindata'),
    ]

    operations = [
        migrations.CreateModel(
            name='DistanceMeasurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='DustbinStatus',
        ),
    ]
