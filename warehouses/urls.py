from django.urls import path
from . import views

urlpatterns = [
    path('addwerehouse/',views.addwarehouse, name='addwerehouse'),
    path('addwerehouse/edit/<int:warehouse_id>',views.editwarehouse, name='editwerehouse'),
    path('addwerehouse/delete/<int:warehouse_id>',views.deletewarehouse, name='deletewerehouse'),
    path('addwerehouse/getstockwerehouse/<int:product_id>',views.getstockwerehouse, name='getstockwerehouse'),
    path('addwerehousepurchasing/',views.addwerehousepurchasing, name='addwerehousepurchasing'),
    path('addwerehousepurchasing/showreportspurchasing/<int:werehousepurchasings_id>',views.showreportpurchasing, name='showreportpurchasing'),
    path('addtypemovement/',views.addtypemovement, name='addtypemovement'),
    path('addtypemovement/edit/<int:typemovement_id>',views.edittypemovement, name='edittypemovement'),
    path('addtypemovement/delete/<int:typemovement_id>',views.deletetypemovement, name='deletetypemovement'),
    path('addtypemovement/gettypemovement/<int:typemovement_id>',views.gettypemovement, name='gettypemovement'),
    path('addwerehouseconcept/',views.addwerehouseconcept, name='addwerehouseconcept'),
    path('addwerehouseconcept/edit/<int:werehouseconcept_id>',views.editwerehouseconcept, name='editwerehouseconcept'),
    path('addwerehouseconcept/delete/<int:werehouseconcept_id>',views.deletewerehouseconcept, name='deletewerehouseconcept'),
    path('addmovementwerehouse/',views.addmovementwerehouse, name='addmovementwerehouse'),
    path('addmovementwerehouse/showreportsmovements/<int:werehousemovement_id>',views.showreportmovements, name='showreportmovements'),
    path('addtransferwerehouse/',views.addtransferwerehouse, name='addtransferwerehouse'),
    
    
]