# Generated by Django 5.1.1 on 2024-11-29 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj_display', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='extrademoschool',
            old_name='school',
            new_name='school_id',
        ),
        migrations.AlterUniqueTogether(
            name='extrademoschool',
            unique_together={('school_id', 'school_year')},
        ),
    ]