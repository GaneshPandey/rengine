# Generated by Django 3.0.6 on 2020-05-31 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startScan', '0015_auto_20200531_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scanactivity',
            name='time',
            field=models.CharField(max_length=100),
        ),
    ]
