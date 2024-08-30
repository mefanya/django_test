from django.shortcuts import get_object_or_404, render

from catalog.models import Product


def products_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "products_list.html", context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, "product_detail.html", context)


def add_product(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        is_available = request.POST.get("is_available") == "true"
        image = request.FILES.get("image")

        Product.objects.create(
            name=name,
            price=price,
            description=description,
            is_available=is_available,
            image=image,
        )
    return render(request, "add_product.html")
