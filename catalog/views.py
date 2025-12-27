import time

from django.shortcuts import render, get_object_or_404

from catalog.models import Product, Category


def main(request):
    return render(request, "main.html")


def contacts(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["messageInput"]
        time.sleep(2)
    return render(request, "contacts.html")


def catalogs(request):
    return render(request, "catalogs.html")


def category(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    return render(request, "category.html", context)


def categories_list(request,category_id):
    products = Product.objects.filter(category=category_id)
    context = {"products": products}
    return render(request, "categories_list.html", context)


def products_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, "products_detail.html", context)

