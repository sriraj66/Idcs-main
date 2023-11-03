# Generated by Django 4.2.6 on 2023-10-30 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_alter_hod_assign_feedback_alter_hod_staffs_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hod',
            name='assign_feedback',
            field=models.ManyToManyField(blank=True, related_name='assign_feed', to='core.staff'),
        ),
        migrations.AlterField(
            model_name='hod',
            name='staffs',
            field=models.ManyToManyField(blank=True, related_name='my_staffs', to='core.staff'),
        ),
        migrations.AlterField(
            model_name='hod',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='students', to='core.student'),
        ),
        migrations.AlterField(
            model_name='individualstaffrating',
            name='ratings',
            field=models.ManyToManyField(blank=True, related_name='StaffRating_Individual', to='core.staffrating'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='my_feedbacks',
            field=models.ManyToManyField(blank=True, related_name='my_ratings', to='core.individualstaffrating'),
        ),
        migrations.AlterField(
            model_name='student',
            name='feedback_for',
            field=models.ManyToManyField(blank=True, related_name='for_staff_rating', to='core.individualstaffrating'),
        ),
        migrations.AlterField(
            model_name='student',
            name='teaching_staffs',
            field=models.ManyToManyField(blank=True, to='core.staff'),
        ),
    ]