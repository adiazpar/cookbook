# Generated by Django 4.2 on 2024-04-26 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook_app', '0011_alter_recipe_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(blank=True, to='cookbook_app.ingredientset'),
        ),
    ]
