from django.urls import path
from . import views as pd
urlpatterns = [
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
]