# Generated by Django 5.0.7 on 2024-07-23 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0007_alter_asset_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='file',
            field=models.FileField(upload_to='media_root/%Y/%MM/e965cceb-8aa0-4210-ae8b-2fcc7c3b2588'),
        ),
    ]