# Generated by Django 4.2.6 on 2023-10-13 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_od_advisor_remove_od_hod_remove_od_mentor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='od',
            old_name='subject',
            new_name='body',
        ),
    ]