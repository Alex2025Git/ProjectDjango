import time

from django.shortcuts import render


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
    return render(request, "category.html")
