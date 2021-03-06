# Generated by Django 2.2.2 on 2020-02-24 13:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import user_manager.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('type', models.CharField(choices=[('s', 'Student'), ('d', 'Doctor')], max_length=1)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', user_manager.models.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='DoctorProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialization', models.CharField(max_length=100)),
                ('mobiles_number', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=500)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_doctor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Hostel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostel_name', models.CharField(max_length=100)),
                ('dean_name', models.CharField(max_length=100)),
                ('hostel_add', models.CharField(max_length=600)),
                ('dean_mobile_number', models.CharField(max_length=100)),
                ('dean_email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthdate', models.DateField()),
                ('gender', models.CharField(choices=[('m', 'male'), ('f', 'female')], max_length=1)),
                ('parent_email', models.EmailField(max_length=100)),
                ('assigned_doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_doctor_profile', to='user_manager.DoctorProfile')),
                ('hostel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hostel_student', to='user_manager.Hostel')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_student', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
