# Generated by Django 2.0.7 on 2018-08-29 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0006_auto_20180829_1141'),
    ]

    operations = [
        migrations.RenameField(
            model_name='software',
            old_name='iGem_team_name',
            new_name='iGemTeamName',
        ),
    ]