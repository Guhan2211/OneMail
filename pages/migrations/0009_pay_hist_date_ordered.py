# Generated by Django 3.0.6 on 2020-06-03 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_pay_hist'),
    ]

    operations = [
        migrations.AddField(
            model_name='pay_hist',
            name='date_ordered',
            field=models.DateTimeField(auto_now=True, verbose_name='Date ordered'),
        ),
    ]
