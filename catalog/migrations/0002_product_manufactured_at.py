# Generated by Django 5.1 on 2024-08-27 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="manufactured_at",
            field=models.DateField(default="2024-08-10", verbose_name="Дата создания"),
        ),
    ]
