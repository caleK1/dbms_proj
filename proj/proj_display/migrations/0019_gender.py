# Generated by Django 5.1.1 on 2024-10-16 00:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj_display', '0018_alter_demographic_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('male', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Male')),
                ('female', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Female')),
                ('school_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='proj_display.school')),
            ],
        ),
    ]