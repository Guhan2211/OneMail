# Generated by Django 3.0.6 on 2020-06-03 14:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('es', '0010_auto_20200603_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email_model',
            name='uid',
            field=models.CharField(auto_created=True, default=uuid.UUID('b608480c-a5a8-11ea-b9ca-7440bb36fee8'), max_length=200),
        ),
    ]
