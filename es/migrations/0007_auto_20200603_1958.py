# Generated by Django 3.0.6 on 2020-06-03 14:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('es', '0006_auto_20200603_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email_model',
            name='uid',
            field=models.CharField(auto_created=True, default=uuid.UUID('7e0686ac-a5a6-11ea-9a53-7440bb36fee8'), max_length=200),
        ),
    ]
