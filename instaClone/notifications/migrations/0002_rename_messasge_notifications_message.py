# Generated by Django 5.0.7 on 2024-10-27 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notifications',
            old_name='messasge',
            new_name='message',
        ),
    ]
