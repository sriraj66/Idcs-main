# Generated by Django 4.2.6 on 2023-10-30 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_alter_student_feedback_for'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='my_feedbacks',
            field=models.ManyToManyField(related_name='my_ratings', to='core.individualstaffrating'),
        ),
    ]
