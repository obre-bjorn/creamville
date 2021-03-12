from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ('name','date_added','p_image','caption','category', 'unit','price') 