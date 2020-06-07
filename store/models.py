from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    imglink = models.CharField(max_length=600)

class Order(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=600)
    city = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=200)
    payment_data = models.CharField(max_length=200)
    items = models.TextField()
    fulfilled = models.BooleanField()