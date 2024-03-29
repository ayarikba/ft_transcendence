# Generated by Django 3.2.11 on 2024-02-19 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='blocked',
        ),
        migrations.AddField(
            model_name='profile',
            name='logged',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='default_profile_picture.jpg', upload_to='avatars/'),
        ),
    ]
