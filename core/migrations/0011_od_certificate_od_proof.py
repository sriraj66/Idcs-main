# Generated by Django 4.2.6 on 2023-10-13 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_rename_status_od_astatus_od_hstatus_od_mstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='od',
            name='certificate',
            field=models.FileField(blank=True, upload_to='od/proof/certificate'),
        ),
        migrations.AddField(
            model_name='od',
            name='proof',
            field=models.FileField(blank=True, upload_to='od/proof'),
        ),
    ]
