# Generated by Django 3.0.6 on 2020-06-01 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_profile_temp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='temp',
            new_name='temp_amnt',
        ),
        migrations.AddField(
            model_name='profile',
            name='temp_mail',
            field=models.IntegerField(default=0),
        ),
    ]
