# Generated by Django 2.2.12 on 2020-12-08 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='user',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='text',
            new_name='title',
        ),
        migrations.AddField(
            model_name='image',
            name='file',
            field=models.FileField(null=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='image',
            name='file_path',
            field=models.CharField(default='media/', max_length=100),
        ),
    ]
