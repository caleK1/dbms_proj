# Generated by Django 5.1.1 on 2024-10-01 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj_display', '0013_rename_schools_in_county_county_districts_in_county'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='county',
            name='districts_in_county',
        ),
        migrations.RemoveField(
            model_name='district',
            name='schools_in_district',
        ),
    ]