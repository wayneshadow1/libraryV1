# Generated by Django 5.0.7 on 2024-07-23 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0008_alter_asset_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='file',
            field=models.FileField(upload_to='media_root/%Y/%MM/13dd1689-270b-47a4-b461-18ed5cf3ad12'),
        ),
    ]
