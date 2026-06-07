from django import forms
from phonenumber_field.modelfields import PhoneNumberField
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

    product = forms.ModelChoiceField(
        queryset=Product.objects.all(),
        widget = forms.Select(attrs={
            'class': 'form-control select2-product',
            'style': 'width: 30%;',
        })
    )
    quantity = forms.IntegerField(
        label='Soni',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'soni',
        })
    )
    price = forms.IntegerField(
        label='Sotish narxi',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',

        })
    )
    owner = forms.CharField(
        label='Sotib oluvchi',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ism familiya',
        })
    )
    owner_phone = forms.CharField(
        label='Sotib oluvchi telefon raqami',
        widget= forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'tel',
            'placeholder': '+998901234567',
        })
    )
    address = forms.CharField(
        label='Yetkazish manzili',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Manzilni aniq kiriting...',
            'rows': '4',
        })
    )
    description = forms.CharField(
        label='Qo\'shimcha ma\'lumot(Ixtiyoriy)',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': "Qo'shimcha malumot bo'lsa shu yerga yozing...",
        })
    )

    class Meta:
        model = SoldProduct
        fields = ('product', 'quantity', 'price', 'owner', 'owner_phone', 'address', 'description')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].label_from_instance = lambda obj: f"{obj.name} - {obj.color} ({obj.son} ta qoldi)"