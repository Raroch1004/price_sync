from django.contrib.auth.models import User
from django.db import models


class Site(models.Model):
    name = models.CharField(max_length=255)
    domain = models.URLField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Site'


class Product(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products', null=True)
    resource_path = models.CharField(max_length=500)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name='products', null=True)

    @property
    def full_url(self):
        return f"{self.site.domain}/{self.resource_path}"

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'


class PriceHistory(models.Model):
    price = models.FloatField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='price_history', null=True)
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.product.name} {self.price} {self.date}"

    class Meta:
        verbose_name = 'PriceHistory'
