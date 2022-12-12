# Generated by Django 4.1 on 2022-12-12 07:19

from django.db import migrations, models
import users.validators


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0015_rename_postlikes_postlike'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='post_image', validators=[users.validators.validate_file_size], verbose_name='Картина'),
        ),
    ]
