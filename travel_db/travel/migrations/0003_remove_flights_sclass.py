# Generated by Django 4.0 on 2023-10-18 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0002_flights_sclass'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flights',
            name='sclass',
        ),
    ]
