from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, ProductModeratorForm
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


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse_lazy('catalog:product_detail', kwargs={'pk': self.object.pk})

    def get_initial(self):
        referer = self.request.META.get('HTTP_REFERER')
        values_dict = {}
        if 'categories' in referer:
            values_dict['category'] = Category.objects.get(pk=referer.split('/')[4])

        return values_dict

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse_lazy('catalog:product_detail', kwargs={'pk': self.object.pk})

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm('can_unpublish_product') and self.object.is_published:
            return ProductModeratorForm
        raise PermissionDenied(self.request, 'Нет прав доступа', 'catalog/errors/403.html')


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:category_list')

    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=self.kwargs.get("pk"))
        if request.user.has_perm('can_unpublish_product') or request.user == product.owner:
            product.delete()
            return redirect('catalog:category_list')
        return HttpResponseForbidden("У вас нет прав для удаления товара.")
