# Generated by Django 4.1.3 on 2022-11-06 13:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(max_length=150)),
                ('surname', models.CharField(max_length=150)),
                ('middle_name', models.CharField(max_length=150)),
                ('birth_date', models.DateField(default='2000-01-01', verbose_name='Birth Date')),
                ('iin_number', models.CharField(max_length=12)),
                ('id_number', models.CharField(max_length=12)),
                ('phone_number', models.CharField(blank=True, max_length=11, null=True)),
                ('department_id', models.CharField(blank=True, max_length=11, null=True)),
                ('specialization_id', models.CharField(blank=True, max_length=11, null=True)),
                ('experience_in_years', models.CharField(max_length=12)),
                ('photo', models.ImageField(upload_to='')),
                ('category', models.CharField(choices=[('j', 'Junior'), ('m', 'Middle'), ('s', 'Senior')], default=None, max_length=20)),
                ('appointment_price', models.CharField(max_length=6)),
                ('shedule_details', models.CharField(blank=True, max_length=500, null=True)),
                ('degree', models.CharField(choices=[('b', 'BS'), ('m', 'MD'), ('p', 'PhD')], default=None, max_length=20)),
                ('rating', models.CharField(max_length=2)),
                ('address', models.CharField(max_length=150)),
                ('homepage_url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(max_length=150)),
                ('surname', models.CharField(max_length=150)),
                ('middle_name', models.CharField(max_length=150)),
                ('birth_date', models.DateField(default='2000-01-01', verbose_name='Birth Date')),
                ('blood_group', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')], default=None, max_length=10)),
                ('iin_number', models.CharField(max_length=12)),
                ('id_number', models.CharField(max_length=12)),
                ('phone_number', models.CharField(blank=True, max_length=11, null=True)),
                ('emergency_phone_number', models.CharField(blank=True, max_length=11, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('address', models.CharField(max_length=150)),
                ('marital_status', models.CharField(choices=[('s', 'Single'), ('m', 'Married'), ('w', 'Widowed'), ('d', 'Divorsed')], default=None, max_length=20)),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]