# Generated by Django 2.0.7 on 2018-08-30 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0015_auto_20180830_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='software',
            name='iGemYear',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
