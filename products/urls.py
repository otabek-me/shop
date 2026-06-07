from os import name

from django.urls import path

from products.views import ProductListView, ProductDetailView, ProductDeleteView, CreateProductView, SkalatListView, \
    SkalatDetailView, SkalatDeleteView, CreateSkalatView, CreateCategoryView, UpdateProductView, SellProductView

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('<slug:slug>', ProductDetailView.as_view(), name='product-detail'),
    path('<slug:slug>/update', UpdateProductView.as_view(), name='product-update'),
    path('<slug:slug>/delete', ProductDeleteView.as_view(), name='product-delete'),
    path('create/', CreateProductView.as_view(), name='create-product'),
    path('sell/', SellProductView.as_view(), name='sell-product'),

    path('skalats/', SkalatListView.as_view(), name='skalat-list'),
    path('skalat/<int:pk>', SkalatDetailView.as_view(), name='skalat-detail'),
    path('skalat/<int:pk>/delete', SkalatDeleteView.as_view(), name='skalat-delete'),
    path('skalat/create/', CreateSkalatView.as_view(), name='create-skalat'),

    path('create/category', CreateCategoryView.as_view(), name='create-category'),
]