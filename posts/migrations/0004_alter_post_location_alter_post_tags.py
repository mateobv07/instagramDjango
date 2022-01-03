# Generated by Django 4.0 on 2022-01-03 00:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_account_phone_number'),
        ('posts', '0003_alter_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='location',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tagged', to='accounts.account'),
        ),
    ]