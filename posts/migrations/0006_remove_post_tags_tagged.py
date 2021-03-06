# Generated by Django 4.0 on 2022-01-06 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_userfollowing_account_description_and_more'),
        ('posts', '0005_saved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.CreateModel(
            name='Tagged',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post')),
                ('tagged_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_by', to='accounts.account')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='accounts.account')),
            ],
        ),
    ]
