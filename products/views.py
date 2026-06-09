from django.utils import timezone
from django.db.models import Sum, F, Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView, TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth import get_user_model
from datetime import timedelta, datetime

from .models import Product, Skalat, Category, SoldProduct
from .forms import (
    CreateProductForm, ProductUpdateForm, CreateSkalatForm,
    CreateCategoryForm, SellProductForm, DeliverSoldProductForm
)

User = get_user_model()


# ==================== ADMIN RUXSATI MIXIN ====================
class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser


# ==================== BOSH SAHIFA ====================
class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        is_authenticated = user.is_authenticated
        is_superuser = user.is_superuser

        # Umumiy statistika (hammaga)
        context['total_products'] = Product.objects.count()
        context['total_skalats'] = Skalat.objects.count()

        # Kam miqdordagi mahsulotlar (faqat autentifikatsiyalangan foydalanuvchilar uchun)
        if is_authenticated:
            context['low_stock_products'] = Product.objects.filter(son__gte=1, son__lte=3).order_by('son')[:10]
        else:
            context['low_stock_products'] = []

        # Sotuvlar bo'yicha ma'lumotlar
        if is_superuser:
            # Admin: barcha sotuvlar
            context['total_sold'] = SoldProduct.objects.count()
            total_profit = SoldProduct.objects.aggregate(
                total=Sum((F('product__tannarx') - F('price')) * F('quantity'))
            )['total']
            context['total_profit'] = total_profit if total_profit else 0
            context['recent_sales'] = SoldProduct.objects.select_related('product', 'seller').order_by('-sold_at')[:5]

            today = timezone.now().date()
            week_dates = [today - timedelta(days=i) for i in range(6, -1, -1)]
            sales_per_day = []
            for date in week_dates:
                count = SoldProduct.objects.filter(sold_at__date=date).count()
                sales_per_day.append(count)
            context['sales_last_week'] = sales_per_day
            context['week_labels'] = [d.strftime('%d.%m') for d in week_dates]

        elif is_authenticated:
            # Oddiy user: faqat o'zi sotgan mahsulotlar
            context['total_sold'] = SoldProduct.objects.filter(seller=user).count()
            total_profit = SoldProduct.objects.filter(seller=user).aggregate(
                total=Sum((F('product__tannarx') - F('price')) * F('quantity'))
            )['total']
            context['total_profit'] = total_profit if total_profit else 0
            context['recent_sales'] = SoldProduct.objects.filter(seller=user).select_related('product').order_by(
                '-sold_at')[:5]

            today = timezone.now().date()
            week_dates = [today - timedelta(days=i) for i in range(6, -1, -1)]
            sales_per_day = []
            for date in week_dates:
                count = SoldProduct.objects.filter(seller=user, sold_at__date=date).count()
                sales_per_day.append(count)
            context['sales_last_week'] = sales_per_day
            context['week_labels'] = [d.strftime('%d.%m') for d in week_dates]

        else:
            # Anonim
            context['total_sold'] = None
            context['total_profit'] = None
            context['recent_sales'] = []
            context['sales_last_week'] = [0] * 7
            context['week_labels'] = [(timezone.now().date() - timedelta(days=i)).strftime('%d.%m') for i in
                                      range(6, -1, -1)]

        return context


# ==================== MAHSULOTLAR (FAQAT ADMIN) ====================
class CreateProductView(AdminRequiredMixin, CreateView):
    model = Product
    template_name = 'products/create_product.html'
    form_class = CreateProductForm
    success_url = reverse_lazy('product-list')


class UpdateProductView(AdminRequiredMixin, UpdateView):
    model = Product
    template_name = 'products/update_product.html'
    form_class = ProductUpdateForm
    success_url = reverse_lazy('product-list')


class ProductDeleteView(AdminRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('product-list')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


# ==================== MAHSULOTLAR RO'YXATI VA DETAL (HAMMA UCHUN) ====================
class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'


# ==================== SOTISH (HAMMA UCHUN) ====================
class SellProductView(LoginRequiredMixin, CreateView):
    model = SoldProduct
    form_class = SellProductForm
    template_name = 'products/sell_product.html'
    success_url = reverse_lazy('product-list')

    def form_valid(self, form):
        form.instance.seller = self.request.user
        sold_item = form.save(commit=False)
        product = sold_item.product
        quantity_sold = form.cleaned_data.get('quantity', 1)

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


# ==================== SKALAT (OMBOR) ====================
class CreateSkalatView(AdminRequiredMixin, CreateView):
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
        context['products'] = self.get_object().products.all()
        return context


class SkalatDeleteView(AdminRequiredMixin, DeleteView):
    model = Skalat
    success_url = reverse_lazy('skalat-list')


# ==================== KATEGORIYA (FAQAT ADMIN) ====================
class CreateCategoryView(AdminRequiredMixin, CreateView):
    model = Category
    form_class = CreateCategoryForm
    template_name = 'products/create_category.html'
    success_url = reverse_lazy('create-product')


# ==================== SOTILGAN MAHSULOTLAR (HAMMA UCHUN) ====================
class SoldProductListView(LoginRequiredMixin, ListView):
    model = SoldProduct
    template_name = 'products/sold_product_list.html'
    context_object_name = 'sold_products'
    ordering = ['-sold_at']

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        queryset = self.get_queryset()
        sum_profit = queryset.aggregate(jami_foyda=Sum((F('product__tannarx') - F('price')) * F('quantity')))['jami_foyda']
        context['sum_profit'] = sum_profit if sum_profit else 0
        return context

    def get_queryset(self):
        result = super().get_queryset()
        start = self.request.GET.get('start')
        end = self.request.GET.get('end')
        filterr = self.request.GET.get('filterr')

        if start and end:
            result = result.filter(sold_at__range=(start, end))
        if filterr:
            result = result.order_by('delievered', '-sold_at')
        return result


class SoldProductDetailView(LoginRequiredMixin, DetailView):
    model = SoldProduct
    template_name = 'products/sold_product_detail.html'
    context_object_name = 'sold_product'


class DeliverSoldProductView(LoginRequiredMixin, UpdateView):
    model = SoldProduct
    template_name = 'products/deliver_sold_product.html'
    success_url = reverse_lazy('sold-products')
    form_class = DeliverSoldProductForm

    def form_valid(self, form):
        sold_item = form.save(commit=False)
        sold_item.delievered_at = timezone.now()
        sold_item.delievered = True
        sold_item.save()
        return super().form_valid(form)


# ==================== ADMIN: FOYDALANUVCHILAR BOSHQARUVI ====================
class AdminUserListView(AdminRequiredMixin, ListView):
    model = User
    template_name = 'products/admin_users.html'
    context_object_name = 'users'
    ordering = ['-date_joined']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        users_data = []
        for user in context['users']:
            users_data.append({
                'user': user,
                'sold_count': user.seller.count(),
                'delivered_count': user.posted_by.filter(delievered=True).count(),
            })
        context['users_data'] = users_data
        return context


class AdminUserDetailView(AdminRequiredMixin, DetailView):
    model = User
    template_name = 'products/admin_user_detail.html'
    context_object_name = 'target_user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['sold_products'] = SoldProduct.objects.filter(seller=user).order_by('-sold_at')[:20]
        context['delivered_products'] = SoldProduct.objects.filter(delievered_by=user, delievered=True).order_by('-delievered_at')[:20]
        context['total_sold'] = user.seller.count()
        context['total_delivered'] = user.posted_by.filter(delievered=True).count()
        context['total_revenue'] = user.seller.aggregate(total=Sum(F('price') * F('quantity')))['total'] or 0
        return context


# ==================== ADMIN: STATISTIKA PANELI ====================
class StoreAnalyticsView(LoginRequiredMixin, TemplateView):
    template_name = 'analytics.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        filters = Q()
        if start_date and end_date:
            filters &= Q(sold_at__date__gte=start_date) & Q(sold_at__date__lte=end_date)

        # KPI
        sold_queryset = SoldProduct.objects.filter(filters)
        total_revenue = sold_queryset.aggregate(total=Sum(F('price') * F('quantity')))['total'] or 0
        total_profit = sold_queryset.aggregate(profit=Sum((F('price') - F('product__tannarx')) * F('quantity')))['profit'] or 0
        total_sales_count = sold_queryset.aggregate(count=Sum('quantity'))['count'] or 0
        pending_value = sold_queryset.filter(delievered=False).aggregate(pending=Sum(F('price') * F('quantity')))['pending'] or 0

        context.update({
            'total_revenue': total_revenue,
            'total_profit': total_profit,
            'total_sales_count': total_sales_count,
            'pending_value': pending_value,
        })

        # Top 5 mahsulot
        top_products = sold_queryset.values(
            'product__id', 'product__name', 'product__color'
        ).annotate(
            total_qty=Sum('quantity'),
            total_profit=Sum((F('price') - F('product__tannarx')) * F('quantity'))
        ).order_by('-total_qty')[:5]
        context['top_products'] = list(top_products)

        # Top lokatsiyalar
        top_places = sold_queryset.values(
            'product__place__name'
        ).annotate(
            revenue=Sum(F('price') * F('quantity'))
        ).filter(product__place__isnull=False).order_by('-revenue')[:5]
        context['top_places'] = list(top_places)

        # Grafik ma'lumotlari (sanalar bo'yicha)
        chart_data = []
        if start_date and end_date:
            start = datetime.strptime(start_date, '%Y-%m-%d').date()
            end = datetime.strptime(end_date, '%Y-%m-%d').date()
            current = start
            while current <= end:
                day_sales = SoldProduct.objects.filter(filters & Q(sold_at__date=current)).aggregate(
                    revenue=Sum(F('price') * F('quantity')),
                    profit=Sum((F('price') - F('product__tannarx')) * F('quantity'))
                )
                chart_data.append({
                    'date': current.strftime('%d.%m'),
                    'revenue': day_sales['revenue'] or 0,
                    'profit': day_sales['profit'] or 0,
                })
                current += timedelta(days=1)
        else:
            today = timezone.now().date()
            for i in range(29, -1, -1):
                day = today - timedelta(days=i)
                day_sales = SoldProduct.objects.filter(sold_at__date=day).aggregate(
                    revenue=Sum(F('price') * F('quantity')),
                    profit=Sum((F('price') - F('product__tannarx')) * F('quantity'))
                )
                chart_data.append({
                    'date': day.strftime('%d.%m'),
                    'revenue': day_sales['revenue'] or 0,
                    'profit': day_sales['profit'] or 0,
                })

        context['chart_labels'] = [item['date'] for item in chart_data]
        context['chart_revenue'] = [item['revenue'] for item in chart_data]
        context['chart_profit'] = [item['profit'] for item in chart_data]

        # Kam qolgan mahsulotlar
        context['low_stock_products'] = Product.objects.filter(son__lt=5).order_by('son')[:10]

        # Filtr qiymatlarini saqlash
        context['start_date'] = start_date or ''
        context['end_date'] = end_date or ''

        return context