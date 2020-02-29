from django.db import models

# Create your models here.
class Product(models.Model):
    id:models.IntegerField()
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=2083)
    price = models.IntegerField()
