# Generated by Django 5.0.7 on 2024-07-25 10:53

import library.storage_backends
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0012_alter_asset_file_alter_asset_publicity_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='file',
            field=models.FileField(storage=library.storage_backends.PublicMediaStorage(), upload_to='%Y/%M/94938599-ad3a-4377-a85c-d9bd30ea64d0'),
        ),
    ]
