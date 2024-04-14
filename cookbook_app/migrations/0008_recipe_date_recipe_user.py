# Generated by Django 4.2 on 2024-04-14 06:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cookbook_app', '0007_alter_ingredientset_ingredient'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='date',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='recipe',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
