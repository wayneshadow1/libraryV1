# Generated by Django 5.0.7 on 2024-07-25 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0013_alter_asset_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='file',
            field=models.FileField(upload_to='%Y/%M/7c2414ab-2eec-48db-aaf5-2ec715c5e3a4'),
        ),
    ]