# Generated by Django 3.2 on 2022-06-21 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_hooks'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hooks',
            old_name='user_id',
            new_name='users_id',
        ),
    ]
