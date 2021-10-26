# Generated by Django 3.2.8 on 2021-10-26 12:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_auto_20211024_1644'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('sap', models.ForeignKey(default='00000000000', max_length=11, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='sap')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dashboard.subject')),
            ],
            options={
                'verbose_name_plural': 'Attendance',
            },
        ),
        migrations.AddField(
            model_name='ica',
            name='sap',
            field=models.ForeignKey(default='00000000000', max_length=11, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='sap'),
        ),
        migrations.CreateModel(
            name='AttendanceReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('attendance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.attendance')),
                ('sap', models.ForeignKey(default='00000000000', max_length=11, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='sap')),
            ],
            options={
                'verbose_name_plural': 'AttendanceReport',
            },
        ),
    ]
