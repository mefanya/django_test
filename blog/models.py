from django.db import models

NULLABLE = {"blank": True, "null": True}


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    slug = models.CharField(max_length=100, verbose_name="slug")
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    image = models.ImageField(
        verbose_name="Изображение", upload_to="blog/images", **NULLABLE
    )
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")
    views_count = models.PositiveIntegerField(
        default=0, verbose_name="Количество просмотров"
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
