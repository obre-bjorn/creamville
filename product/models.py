from django.db import models

# Create your models here.
class Product(models.Model):
    """ Product to be sold """
    name    = models.CharField(max_length = 200)
    price  