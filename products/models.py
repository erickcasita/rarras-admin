from django.db import models

# Create your models here.

# Create your models here.
class Categories (models.Model):
    name = models.CharField(max_length=30)
    sat =  models.CharField(max_length=10)
    umedida = models.CharField(max_length=4)
    visible = models.BooleanField(default=True)
    created  = models.DateTimeField(auto_now_add=True)
    #usercreated = models.ForeignKey(User, on_delete= models.RESTRICT)
    
    def __str__(self):
        return self.name 

class Brands (models.Model):
    name = models.CharField(max_length=30)
    categories = models.ForeignKey(Categories, on_delete= models.RESTRICT)
    visible = models.BooleanField(default=True)
    created  = models.DateTimeField(auto_now_add=True)
    #usercreated = models.ForeignKey(User, on_delete= models.RESTRICT)
    
    def __str__(self):
        return self.name 

class Products (models.Model):
    name = models.CharField(max_length=60)
    categories = models.ForeignKey(Categories, on_delete= models.RESTRICT)
    brands = models.ForeignKey(Brands, on_delete= models.RESTRICT)
    cvesap = models.CharField(max_length=10)
    visible = models.BooleanField(default=True)
    created  = models.DateTimeField(auto_now_add=True)
    #usercreated = models.ForeignKey(User, on_delete= models.RESTRICT)
    
    def __str__(self):
        return self.name 
    
class ProductList (models.Model):
    
    name = models.CharField(max_length=60)
    visible = models.BooleanField(default=True)
    created  = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class ProductListDetails (models.Model):
    productlist = models.ForeignKey(ProductList, on_delete= models.RESTRICT)
    product = models.ForeignKey(Products, on_delete= models.RESTRICT)
    predlp = models.FloatField()
    created  = models.DateTimeField(auto_now_add=True)