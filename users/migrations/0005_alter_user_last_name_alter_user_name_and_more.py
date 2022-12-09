# Generated by Django 4.1 on 2022-12-08 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='test', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default='test', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(null=True, upload_to='user_profile'),
        ),
    ]