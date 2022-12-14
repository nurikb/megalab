# Generated by Django 4.1 on 2022-12-08 09:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_last_name_alter_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='user_profile'),
            preserve_default=False,
        ),
    ]
