# Generated by Django 4.2.6 on 2023-10-13 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_rename_subject_od_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='od',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=50),
        ),
    ]