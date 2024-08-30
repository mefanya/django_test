from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import index

app_name = CatalogConfig.name

urlpatterns = [
    path("", index),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
