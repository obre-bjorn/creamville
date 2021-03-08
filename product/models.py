from django.db import models

# Create your models here.

CATEGORY_CHOICE = ('Cakes','Cookies','Pastries')


class Product(models.Model):

    CAKE        = 1
    SNACK       = 2
    PASTRY      = 3

    P_CHOICES   = (
        (CAKE, ('Cakes')),
        (SNACK, ('Snacks')),
        (PASTRY, ('Pastry')),
    )

    """ Product to be sold """
    
    name        = models.CharField(max_length = 200)
    date_added  = models.DateTimeField(auto_now_add = True)
    weight      = models.FloatField(max_length = 10)
    caption     = models.TextField()
    category    = models.CharField(choices = P_CHOICES,default = CAKE, max_length = 10)
    price       = models.FloatField()
    
    


    """ Return a string representation of the model """
    
    def __str__(self):
        return self.name
    