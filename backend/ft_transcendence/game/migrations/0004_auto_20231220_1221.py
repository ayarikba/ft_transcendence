# Generated by Django 3.2.11 on 2023-12-20 12:21

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('game', '0003_auto_20231220_1209'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Message',
            new_name='Game_Message',
        ),
        migrations.RenameModel(
            old_name='Room',
            new_name='Game_Room',
        ),
    ]