# Generated by Django 4.2.6 on 2023-10-13 05:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_staff_profile_student_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='od',
            name='advisor',
        ),
        migrations.RemoveField(
            model_name='od',
            name='hod',
        ),
        migrations.RemoveField(
            model_name='od',
            name='mentor',
        ),
    ]
