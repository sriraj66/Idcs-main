# Generated by Django 4.2.6 on 2023-11-01 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_hod_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='section',
            field=models.PositiveIntegerField(choices=[(0, 'Artificial Intelliegnence and Machine Learninig'), (1, 'Artificial Intelliegnence and Data Science'), (2, 'A'), (3, 'B'), (4, 'C'), (5, 'none')], default=5),
        ),
        migrations.AlterField(
            model_name='hod',
            name='department',
            field=models.PositiveIntegerField(choices=[(0, 'B-Tech Artificial Intelliegnence'), (1, 'BE Computer Science and Engineering'), (2, 'None')], default=2, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='department',
            field=models.PositiveIntegerField(choices=[(0, 'B-Tech Artificial Intelliegnence'), (1, 'BE Computer Science and Engineering'), (2, 'None')], default=0, null=True),
        ),
    ]
