""" Defines URL patterns for product """

from django.urls import path

from . import views

urlpatterns = [
    path('product/api/', views.ProductListCreate.as_view())
]



