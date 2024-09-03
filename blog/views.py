from django.db.models.base import Model as Model
from pytils.translit import slugify
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from blog.models import Article


class BlogListView(ListView):
    model = Article

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        return queryset.filter(is_published=True)


class BlogDetailView(DetailView):
    model = Article

    def get_object(self, queryset=None) -> Model:
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = Article
    fields = ("title", "content", "slug", "image", "is_published")

    def form_valid(self, form):
        if form.is_valid():
            new_article = form.save(commit=False)
            new_article.slug = slugify(new_article.title)
            new_article = form.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse("blog:article_detail", args=[self.object.slug])


class BlogUpdateView(UpdateView):
    model = Article
    fields = ("title", "content", "slug", "image", "is_published")

    def form_valid(self, form):
        if form.is_valid():
            new_article = form.save(commit=False)
            new_article.slug = slugify(new_article.title)
            new_article = form.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse("blog:article_detail", args=[self.object.slug])


class BlogDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy("blog:article_list")
