# Generated by Django 2.0.7 on 2018-08-29 17:23

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0003_auto_20180829_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='software',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
