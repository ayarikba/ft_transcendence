# Generated by Django 4.2.10 on 2024-02-24 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0003_profile_avatar_42"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="bio",
            field=models.TextField(blank=True, default="selam", max_length=500),
        ),
    ]
