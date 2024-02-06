# Generated by Django 5.0.1 on 2024-02-06 04:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("implementation", "0002_alter_recipe_recipe_image"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="recipe",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="recipe_image",
            field=models.ImageField(
                blank=True, null=True, upload_to="implementation/images_rec/"
            ),
        ),
    ]
