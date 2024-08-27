from django.core.management import BaseCommand
import os
import json
import chardet

from catalog.models import Product, Category

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "../../fixtures/catalog_data.json")


class Command(BaseCommand):

    @staticmethod
    def json_read_categories(data):
        return [item for item in data if item["model"] == "catalog.category"]

    @staticmethod
    def json_read_products(data):
        return [item for item in data if item["model"] == "catalog.product"]

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        with open(file_path, "rb") as file:
            raw_data = file.read()
            result = chardet.detect(raw_data)
            encoding = result["encoding"]

        decoded_data = raw_data.decode(encoding)
        data = json.loads(decoded_data)

        product_for_create = []
        category_for_create = []

        for category_data in self.json_read_categories(data):
            fields = category_data["fields"]
            category_for_create.append(
                Category(
                    id=category_data["pk"],
                    name=fields["name"],
                    description=fields.get("description", ""),
                )
            )

        Category.objects.bulk_create(category_for_create, ignore_conflicts=True)

        category_dict = {cat.id: cat for cat in Category.objects.all()}

        for product_data in self.json_read_products(data):
            fields = product_data["fields"]
            product_for_create.append(
                Product(
                    name=fields["name"],
                    price=fields["price"],
                    description=fields.get("description", ""),
                    image=fields.get("image", ""),
                    is_available=fields["is_available"],
                    created_at=fields["created_at"],
                    updated_at=fields["updated_at"],
                    category=category_dict[fields["category"]],
                )
            )

        Product.objects.bulk_create(product_for_create)
