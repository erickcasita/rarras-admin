from django.db import models
from warehouses.models import WareHouses
from django.contrib.auth.models import User
# Create your models here.
class TypeUser (models.Model):
    name = models.CharField(max_length=50)
    created  = models.DateTimeField(auto_now_add=True)
    #usercreated = models.ForeignKey(User, on_delete= models.RESTRICT)
    
    def __str__(self):
        return self.name 
    
class ProfileUser(models.Model):
    user = models.OneToOneField(User, on_delete= models.RESTRICT)
    typeuser = models.ForeignKey(TypeUser, on_delete= models.RESTRICT)
    warehouse = models.ManyToManyField(WareHouses)
    created  = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username