# Generated by Django 3.2.14 on 2022-07-18 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0009_uploadedfile_file_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedfile',
            name='file_type',
            field=models.CharField(default=11, max_length=50),
            preserve_default=False,
        ),
    ]
