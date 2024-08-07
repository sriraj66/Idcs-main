# Generated by Django 4.2.6 on 2023-10-18 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_remove_gatepass_certificate_remove_gatepass_proof'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='teaching_staffs',
            field=models.ManyToManyField(to='core.staff'),
        ),
        migrations.CreateModel(
            name='StaffRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.PositiveIntegerField(default=0)),
                ('comments', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.staff')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.student')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
