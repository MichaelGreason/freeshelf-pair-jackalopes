# Generated by Django 4.1.7 on 2023-03-08 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_resources'),
    ]

    operations = [
        migrations.AddField(
            model_name='resources',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
