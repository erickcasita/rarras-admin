"""
URL configuration for rarrasadmin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from warehouses import views
from products import views as pd
from profileuser import views as pusr
from reports import views as rp
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pusr.signin, name='root'),
    
    path('signin/', pusr.signin, name='signin'),
    path('signout/', pusr.signout, name='signout'),
    path('', include('warehouses.urls')),
    path('addcategories/',pd.addCategories, name='addcategories'),
    path('addcategories/edit/<int:categories_id>',pd.editCategories, name='editcategories'),
    path('addcategories/delete/<int:categories_id>',pd.deleteCategories, name='deletecategories'),
    path('addbrands/',pd.addBrands, name='addbrands'),
    path('addbrands/edit/<int:brands_id>',pd.editBrands, name='editbrands'),
    path('addbrands/delete/<int:brands_id>',pd.deletebrands, name='deletebrands'),
    path('addproducts/',pd.addProducts, name='addproducts'),
    path('addproducts/edit/<int:products_id>',pd.editproduct, name='editproduct'),
    path('addproducts/delete/<int:products_id>',pd.deleteproduct, name='deleteproduct'),
    path('addproductslist/',pd.addProductList, name='addproductlist'),
    path('addproductslist/edit/<int:productlist_id>',pd.editproductslist, name='editproductslist'),
    path('addproductlist/getpriceproduct/<int:product_id>',pd.getpriceproduct, name='getpriceproduct'),
    path('addproducts/getwerehousesproduct/<int:product_id>',pd.getwerehousesproduct, name='getwerehousesproduct'),
    path('addproducts/getstockproduct/<int:product_id>',pd.getstockproduct, name='getstockproduct'),
    path('reportstock/',rp.reportstock, name='reportstock'),
    path('reportmovement/',rp.reportmovement, name='reportmovement'),
    
]
