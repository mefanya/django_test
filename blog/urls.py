from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from blog.apps import BlogConfig
from blog.views import (
    BlogCreateView,
    BlogDeleteView,
    BlogDetailView,
    BlogListView,
    BlogUpdateView,
)

app_name = BlogConfig.name

urlpatterns = [
    path("blog/", BlogListView.as_view(), name="article_list"),
    path("article/create/", BlogCreateView.as_view(), name="article_create"),
    path("article/<slug:slug>/", BlogDetailView.as_view(), name="article_detail"),
    path(
        "article/update/<slug:slug>/", BlogUpdateView.as_view(), name="article_update"
    ),
    path(
        "article/delete/<slug:slug>/", BlogDeleteView.as_view(), name="article_delete"
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
