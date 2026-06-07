import uuid
from django.db import models
from django.utils.text import slugify
from users.models import User
from phonenumber_field.modelfields import PhoneNumberField

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Skalat(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=30)
    tannarx = models.PositiveIntegerField()
    sotish = models.PositiveIntegerField(null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    color = models.CharField(max_length=20)
    place = models.ForeignKey(Skalat, on_delete=models.PROTECT, null=True, blank=True, related_name='products', unique=True)
    slug = models.SlugField(blank=True, null=True, unique=True)
    description = models.TextField(blank=True, null=True)
    son = models.IntegerField(default=0)

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.name)

            if Product.objects.filter(slug=self.slug).exists():
                self.slug = f"{self.slug}-{str(uuid.uuid4())[:6]}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class SoldProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='sales')
    seller = models.ForeignKey(User, on_delete=models.PROTECT, related_name='seller')
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    sold_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    delievered_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='posted_by', blank=True, null=True)
    delievered = models.BooleanField(default=False)
    delievered_at = models.DateTimeField(auto_now_add=True)
    owner = models.CharField(blank=True, null=True, max_length=100)
    owner_phone = PhoneNumberField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    @property
    def profit(self):
        return (self.product.tannarx - self.price) * self.quantity