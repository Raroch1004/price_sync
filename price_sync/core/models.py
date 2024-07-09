from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    path_segment = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Site(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class PriceHistory(models.Model):
    price = models.FloatField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.product.name} {self.price} {self.date}"