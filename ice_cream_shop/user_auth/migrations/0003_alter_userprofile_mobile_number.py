# Generated by Django 3.2.16 on 2023-10-11 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0002_alter_userprofile_mobile_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='mobile_number',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
