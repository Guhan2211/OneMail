# Generated by Django 3.0.6 on 2020-06-03 14:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('es', '0004_auto_20200603_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email_model',
            name='uid',
            field=models.CharField(auto_created=True, default=uuid.UUID('730cea9e-a5a5-11ea-829e-7440bb36fee8'), max_length=200),
        ),
    ]
