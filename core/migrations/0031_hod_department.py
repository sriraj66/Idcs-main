# Generated by Django 4.2.6 on 2023-11-01 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_student_feedback_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='hod',
            name='department',
            field=models.PositiveIntegerField(choices=[(0, 'B-Tech Artificial Intelliegnence'), (1, 'BE Computer Science and Engineering')], default=0, null=True),
        ),
    ]