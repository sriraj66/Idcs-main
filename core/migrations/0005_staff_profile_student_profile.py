# Generated by Django 4.2.6 on 2023-10-12 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_od_leave'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='profile',
            field=models.ImageField(blank=True, upload_to='profiles'),
        ),
        migrations.AddField(
            model_name='student',
            name='profile',
            field=models.ImageField(blank=True, upload_to='profiles'),
        ),
    ]