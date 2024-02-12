from django.urls import path
from . import views

urlpatterns = [
    path('reportstock/',views.reportstock, name='reportstock'),
    path('reportmovement/',views.reportmovement, name='reportmovement'),
    path('reportproducts/',views.reportproducts, name='reportproducts'),
    path('reportpricelist/',views.reportpricelist, name='reportpricelist'),
]