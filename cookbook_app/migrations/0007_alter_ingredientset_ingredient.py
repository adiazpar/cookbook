# Generated by Django 4.2 on 2024-04-14 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook_app', '0006_alter_ingredientset_ingredient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredientset',
            name='ingredient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cookbook_app.ingredient'),
        ),
    ]