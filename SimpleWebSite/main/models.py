import django.db.models
from django.db import models


# Create your models here.
class ProductModel(models.Model):
    ProductName = models.CharField(max_length=256, help_text="Enter product name", default="noname")
    ProductPrice = models.IntegerField(help_text="Enter product price", default=0)
    ProductImage = models.ImageField(null=True, blank=True)
    ProductDescription = models.CharField(max_length=2048, help_text="Enter product description", default="no "
                                                                                                          "description")

    def __str__(self):
        return self.ProductName


class BasketModel(models.Model):
    products = models.ForeignKey(ProductModel, on_delete=models.CASCADE, default='', blank=True, null=True)