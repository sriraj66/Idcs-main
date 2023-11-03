# Generated by Django 4.2.6 on 2023-10-17 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_leave'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='certificate',
            field=models.FileField(blank=True, upload_to='leave/proof/certificate'),
        ),
        migrations.AlterField(
            model_name='leave',
            name='proof',
            field=models.FileField(blank=True, upload_to='leave/proof'),
        ),
    ]
