# Generated by Django 5.0.7 on 2024-07-23 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0003_alter_asset_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='file',
            field=models.FileField(upload_to='media_root/%Y/%MM/29b367c1-e8fc-4f11-acad-58c533b0f721'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='publicity_status',
            field=models.CharField(choices=[('PUBLIC', 'PUBLIC'), ('PRIVATE', 'PRIVATE'), ('FAMILY', 'FAMILY'), ('FRIENDS', 'FRIENDS')], default='PRIVATE', max_length=100),
        ),
    ]
