# Generated by Django 5.1 on 2024-08-27 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0003_alter_product_manufactured_at"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="manufactured_at",
        ),
    ]
