# Generated by Django 5.1.1 on 2024-10-16 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj_display', '0017_demographic_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demographic',
            name='year',
            field=models.CharField(max_length=10, verbose_name='School Year'),
        ),
    ]