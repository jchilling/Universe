# Generated by Django 4.2.2 on 2023-06-21 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='currency',
            field=models.CharField(default=None, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stock',
            name='exchange',
            field=models.CharField(default=None, max_length=10),
            preserve_default=False,
        ),
    ]