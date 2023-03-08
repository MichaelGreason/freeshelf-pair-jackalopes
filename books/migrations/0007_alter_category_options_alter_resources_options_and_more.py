# Generated by Django 4.1.7 on 2023-03-08 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_category_remove_resources_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='resources',
            options={'verbose_name_plural': 'Resources'},
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]