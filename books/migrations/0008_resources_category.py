# Generated by Django 4.1.7 on 2023-03-09 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_alter_category_options_alter_resources_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='resources',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.category'),
        ),
    ]