# Generated by Django 4.2 on 2024-04-14 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook_app', '0009_rename_title_recipe_name_recipe_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='date',
        ),
    ]