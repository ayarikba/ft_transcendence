# Generated by Django 3.2.11 on 2023-12-20 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GamePos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('y_pos_left', models.IntegerField()),
                ('y_pos_right', models.IntegerField()),
                ('ball_x', models.IntegerField()),
                ('ball_y', models.IntegerField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('date_added',),
            },
        ),
        migrations.DeleteModel(
            name='Game_Pos',
        ),
        migrations.DeleteModel(
            name='Game_Room',
        ),
    ]