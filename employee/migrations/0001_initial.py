# Generated by Django 3.2 on 2022-06-21 09:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('tole', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=120)),
                ('zip_code', models.IntegerField()),
                ('country', models.CharField(max_length=120)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EmergencyContact',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=120)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('actions_performed', models.CharField(max_length=225)),
                ('detail', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('full_name', models.CharField(max_length=150)),
                ('attendance', models.IntegerField()),
                ('id_card', models.IntegerField()),
                ('driving_licence', models.IntegerField()),
                ('blood_group', models.CharField(max_length=10)),
                ('salary', models.IntegerField()),
                ('emp_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='emp_data', to='employee.address')),
                ('emp_emergency_contact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='emp_data1', to='employee.emergencycontact')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
