from django.db import models

# Create your models here.
class Product(models.Model):
    """ Product to be sold """
    name        = models.CharField(max_length = 200)
    date_added  = models.DateTimeField(auto_now_add = True)
    weight      = models.FloatField(max_length =)
    price       = models.FloatField
    category    =
    image       = models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None) 