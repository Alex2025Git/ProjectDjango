from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm
from catalog.models import Product, Category


class MainTemplateView(TemplateView):
    template_name = "catalog/main.html"


class ContactsTemplateView(TemplateView):
    template_name = "catalog/contacts.html"

    # if request.method == "POST":
    #     name = request.POST["name"]
    #     email = request.POST["email"]
    #     message = request.POST["messageInput"]
    #     time.sleep(2)
    # return render(request, "catalog/contacts.html")


class CatalogsTemplateView(TemplateView):
    template_name = "catalog/catalogs.html"


class CategoryListView(ListView):
    model = Category


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        return Product.objects.filter(category_id=self.kwargs.get("category_id"))


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse_lazy('catalog:product_detail', kwargs={'pk': self.object.pk})

    def get_initial(self):
        referer = self.request.META.get('HTTP_REFERER')
        if 'categories' in referer:
            return {'category': Category.objects.get(pk=referer.split('/')[4])}
        return {}


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse_lazy('catalog:product_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:category_list')
