# Generated by Django 4.0 on 2022-01-01 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_userprofile_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='account',
            name='last_name',
        ),
        migrations.AddField(
            model_name='account',
            name='real_name',
            field=models.CharField(default='default_name', max_length=100),
        ),
    ]
