from itertools import product

from django.db.models import Sum, F
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from .models import Product, Skalat, Category, SoldProduct
from .forms import CreateProductForm, ProductUpdateForm, CreateSkalatForm, CreateCategoryForm, SellProductForm


class CreateProductView(CreateView):
    model = Product
    template_name = 'products/create_product.html'
    form_class = CreateProductForm
    success_url = reverse_lazy('product-list')

class UpdateProductView(UpdateView):
    model = Product
    template_name = 'products/update_product.html'
    form_class = ProductUpdateForm
    success_url = reverse_lazy('product-list')

class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('product-list')

class SellProductView(CreateView):
    model = SoldProduct
    form_class = SellProductForm
    template_name = 'products/sell_product.html'
    success_url = reverse_lazy('product-list')

    def form_valid(self, form):
        form.instance.seller = self.request.user

        sold_item = form.save(commit=False)
        product = sold_item.product

        quantity_sold = form.cleaned_data.get('quantity_sold', 1)

        if product.son >= quantity_sold:
            product.son -= quantity_sold
            product.save()
        else:
            form.add_error('product', "Mahsulot yetarli emas!")
            return self.form_invalid(form)

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context



class CreateSkalatView(CreateView):
    model = Skalat
    template_name = 'products/create_skalat.html'
    form_class = CreateSkalatForm
    success_url = reverse_lazy('skalat-list')

class SkalatListView(ListView):
    model = Skalat
    template_name = 'products/skalat_list.html'
    context_object_name = 'skalats'

class SkalatDetailView(DetailView):
    model = Skalat
    template_name = 'products/skalat_detail.html'
    context_object_name = 'skalat'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        skalat_object = self.get_object()

        context['products'] = skalat_object.products.all()
        return context

class SkalatDeleteView(DeleteView):
    model = Skalat
    success_url = reverse_lazy('skalat-list')


class CreateCategoryView(CreateView):
    model = Category
    form_class = CreateCategoryForm
    template_name = 'products/create_category.html'
    success_url = reverse_lazy('create-product')

class SoldProductListView(ListView):
    model = SoldProduct
    template_name = 'products/sold_product_list.html'
    context_object_name = 'sold_products'
    ordering = ['-sold_at']

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        queryset = self.get_queryset()

        sum_profit = queryset.aggregate(jami_foyda = Sum((F('product__tannarx') - F('price')) * F('quantity')))['jami_foyda']

        context['sum_profit'] = sum_profit
        return context