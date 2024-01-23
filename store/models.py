from django.db import models

# Create your models here.

class Store (models.Model):
    name = models.CharField(max_length=50)
    street = models.CharField(max_length=200)
    ext = models.CharField(max_length=3,blank=True)
    development = models.CharField(max_length=50)
    region = models.CharField(max_length=50 )
    eststore = models.BooleanField(default=True)
    created  = models.DateTimeField(auto_now_add=True)
    #usercreated = models.ForeignKey(User, on_delete= models.RESTRICT)
    
    def __str__(self):
        return self.name 