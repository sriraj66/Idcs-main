# Generated by Django 4.2.6 on 2023-11-02 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0038_hod_spot_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='spotfeedback',
            name='sompleted_students',
            field=models.ManyToManyField(blank=True, related_name='c_std', to='core.student'),
        ),
    ]
