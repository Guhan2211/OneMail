# Generated by Django 3.0.6 on 2020-06-03 14:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('es', '0009_auto_20200603_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email_model',
            name='uid',
            field=models.CharField(auto_created=True, default=uuid.UUID('e29c7d68-a5a7-11ea-9fc9-7440bb36fee8'), max_length=200),
        ),
    ]
