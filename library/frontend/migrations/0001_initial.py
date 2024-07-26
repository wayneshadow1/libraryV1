# Generated by Django 5.0.6 on 2024-07-11 07:58

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='asset_grouping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Group_name', models.CharField(default=None, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='asset_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default=None, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='asset',
            fields=[
                ('item_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='media_root/%YYYY/%MM')),
                ('publicity_status', models.CharField(choices=[('PUBLIC', 'PUBLIC'), ('PRIVATE', 'PRIVATE')], default='PRIVATE', max_length=100)),
                ('description', models.TextField(default='No descrition')),
                ('author', models.CharField(default='author', max_length=100)),
                ('asset_item_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.asset_grouping')),
                ('asset_item_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.asset_type')),
            ],
        ),
    ]