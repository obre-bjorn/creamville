from django.db import models


# Product choices.

CATEGORY_CHOICE = (
    ('Cakes','Cakes'),
    ('Snacks','Snacks'),
    ('Pastries','Pastries')
)


# Create your models here.


class Product(models.Model):
 

    """ Product to be sold """
    
    name        = models.CharField(max_length = 200)
    date_added  = models.DateTimeField(auto_now_add = True)
    weight      = models.FloatField(max_length = 10)
    p_image     = models.ImageField(upload_to = 'images/',null = True )
    caption     = models.TextField()
    category    = models.CharField(choices = CATEGORY_CHOICE,null = True, max_length = 10)
    price       = models.FloatField()
    
    


    """ Return a string representation of the model """
    
    
    class Meta:
         verbose_name_plural = 'Products'
        
    def __str__(self):
        return self.name
    