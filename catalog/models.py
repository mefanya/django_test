from django.db import models


NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
    name = models.CharField(
        max_length=25, verbose_name="Категория", help_text="Введите название категории"
    )
    description = models.TextField(verbose_name="Описание категории")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        related_name="products",
        **NULLABLE,
    )
    name = models.CharField(
        max_length=25, verbose_name="Продукт", help_text="Введите название продукта"
    )
    price = models.IntegerField(verbose_name="Цена", help_text="Введите целое число")
    description = models.TextField(
        verbose_name="Описание товара",
    )
    image = models.ImageField(
        upload_to="catalog/images",
        verbose_name="Изображение",
        **NULLABLE,
    )
    is_available = models.BooleanField(default=True, verbose_name="В наличии")
    created_at = models.DateField(
        auto_now_add=True, verbose_name="Дата создания", editable=False
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата создания", editable=False
    )
    views_count = models.PositiveIntegerField(
        default=0, verbose_name="Количество просмотров"
    )

    def __str__(self):
        return (
            f"Название: {self.name}, Наличие: {self.is_available}, Цена: {self.price}"
        )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
