from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import products_list, product_detail, add_product

app_name = CatalogConfig.name

urlpatterns = [
    path("", products_list, name="products_list"),
    path("product/<int:pk>/", product_detail, name="product_detail"),
    path("add_product/", add_product, name="add_product"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
