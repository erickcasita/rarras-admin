from django.db import models
from store.models import Store
from products.models import Products
from django.contrib.auth.models import User
# Create your models here.
class TypeMovement (models.Model):
    name = models.CharField(max_length=15)
    visible = models.BooleanField(default=True)
    created  = models.DateTimeField(auto_now_add=True)
    addition = models.BooleanField()
    #usercreated = models.ForeignKey(User, on_delete= models.RESTRICT)
    
    def __str__(self):
        return self.name 

class WareHouseConcept (models.Model):
    title = models.CharField(max_length=50)
    typemovement = models.ForeignKey(TypeMovement, on_delete= models.RESTRICT)
    description = models.TextField(max_length=50,blank=True)
    visible = models.BooleanField(default=True)
    created  = models.DateTimeField(auto_now_add=True)
    #usercreated = models.ForeignKey(User, on_delete= models.RESTRICT)
    
    def __str__(self):       
        return self.title

class WareHouses (models.Model):
    title = models.CharField(max_length=50)
    store = models.ForeignKey(Store, on_delete= models.RESTRICT)
    visible = models.BooleanField(default=True)
    created  = models.DateTimeField(auto_now_add=True)
    #usercreated = models.ForeignKey(User, on_delete= models.RESTRICT)
    def __str__(self):
        return self.title
class WereHouseStock(models.Model):
    werehouse  = models.ForeignKey(WareHouses, on_delete= models.RESTRICT)
    stock = models.BigIntegerField()
    product  = models.ForeignKey(Products, on_delete= models.RESTRICT)
    created  = models.DateTimeField(auto_now_add=True)
    
class WereHouseMovement(models.Model):
    created  = models.DateTimeField(auto_now_add=True)
    werehouse  = models.ForeignKey(WareHouses, on_delete= models.RESTRICT)
    werehouseconcept = models.ForeignKey(WareHouseConcept, on_delete= models.RESTRICT)
    typemovement = models.ForeignKey(TypeMovement, on_delete= models.RESTRICT)
    usercreated = models.ForeignKey(User, on_delete= models.RESTRICT)
    observations = models.TextField(max_length=150,blank=True)

class WereHouseMovementDetails(models.Model):
    werehousemovement = models.ForeignKey(WereHouseMovement, on_delete= models.RESTRICT)
    canmov = models.BigIntegerField()
    created  = models.DateTimeField(auto_now_add=True)
    product  = models.ForeignKey(Products, on_delete= models.RESTRICT)
    usercreated = models.ForeignKey(User, on_delete= models.RESTRICT)
    
class WereHousePurchasing(models.Model):
    fecrem  = models.DateField()
    created =  models.DateTimeField(auto_now_add=True)
    usercreated = models.ForeignKey(User, on_delete= models.RESTRICT)
    totcom = models.FloatField()
    observations = models.TextField(max_length=150,blank=True)
    
class WereHousePurchasingDetails(models.Model):
    werehousepurchasing = models.ForeignKey(WereHousePurchasing, on_delete= models.RESTRICT)
    candco = models.BigIntegerField()
    product = models.ForeignKey(Products, on_delete= models.RESTRICT)
    totdco  = models.FloatField()
    predco  = models.FloatField()
