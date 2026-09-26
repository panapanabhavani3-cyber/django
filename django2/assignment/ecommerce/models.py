from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_code = models.CharField(max_length=50, unique=True)
    category = models.CharField(max_length=100)
    price = models.IntegerField()
    stock_quantity = models.IntegerField()
    description = models.CharField(max_length=500)
    is_available = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name