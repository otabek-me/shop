from django import forms

from products.models import Product, Skalat, Category, SoldProduct


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'name', 'description', 'color', 'place', 'tannarx', 'sotish', 'son')

class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'name', 'description', 'color', 'place', 'tannarx', 'sotish', 'son')

class CreateSkalatForm(forms.ModelForm):
    class Meta:
        model = Skalat
        fields = ('name',)

class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)

class SellProductForm(forms.ModelForm):
    class Meta:
        model = SoldProduct
        fields = ('product', 'quantity', 'price', 'owner', 'owner_phone', 'address', 'description')
