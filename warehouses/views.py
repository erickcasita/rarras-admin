from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .forms import AddWareHouse, AddTypeMovement,AddWareHouseConcept
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import json
from .models import WareHouses, TypeMovement, WareHouseConcept,WereHouseStock,WereHouseMovement,WereHouseMovementDetails,WereHousePurchasing,WereHousePurchasingDetails
from django.contrib.auth.models import User
from django.db.models import Sum
from products.models import ProductList
from helpers.helpers import stockproduct
#reports
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
# Create your views here.

@login_required
def addwarehouse (request):
    if request.method ==  'GET':
        warehouses = WareHouses.objects.filter(visible=True)
        return render(request, 'addwerehouses.html', {
            'form': AddWareHouse,
            'warehouses': warehouses
         })
    else:
        form = AddWareHouse(request.POST)
        if (form.is_valid()):
            newwarehouse =  form.save(commit=False)
            newwarehouse.save()
            messages.success(request,"Almacen creado satisfactoriamente")
            return HttpResponseRedirect('')
        else:
            messages.error(request,"Error en el formulario / revise los datos de registro")
            return HttpResponseRedirect('')    
@login_required
def editwarehouse (request, warehouse_id):
    if request.method ==  'GET':
        
        warehouse =  get_object_or_404(WareHouses,pk=warehouse_id, visible=True)
        form = AddWareHouse(instance=warehouse)
        return render(request, 'editwerehouses.html', {
            'form':form
        })
    else :
        try:
            warehouse =  get_object_or_404(WareHouses,pk=warehouse_id, visible=True)
            form = AddWareHouse(request.POST,instance=warehouse)
            form.save()
            messages.success(request,"Almacen editado satisfactoriamente")
            return HttpResponseRedirect('/addwerehouse/')
        
        except ValueError:
            messages.success(request,"Error al actualizar el campo ")
            return HttpResponseRedirect('/addwerehouse/')
@login_required     
def deletewarehouse(request, warehouse_id):
  
    try:
        warehouse =  get_object_or_404(WareHouses,pk=warehouse_id, visible=True)
        warehouse.visible = False
        warehouse.save()
        messages.success(request,"Almacen eliminado satisfactoriamente")
        return HttpResponseRedirect('/addwerehouse/')
        
    except ValueError:
        messages.success(request,"Error al actualizar el campo ")
        return HttpResponseRedirect('/addwerehouse/')

@login_required
def addtypemovement(request):
    
    if request.method ==  'GET':
        typemovement = TypeMovement.objects.filter(visible=True)
        return render(request, 'addtypemovement.html', {
            'form': AddTypeMovement,
            'typemovement': typemovement
         })
    else:
        form = AddTypeMovement(request.POST)
        if (form.is_valid()):
            newtypemovement =  form.save(commit=False)
            newtypemovement.save()
            messages.success(request,"Tipo de movimiento creado correctamente")
            return HttpResponseRedirect('')
        else:
            messages.error(request,"Error en el formulario / revise los datos de registro")
            return HttpResponseRedirect('')       
@login_required
def getstockwerehouse(request, product_id):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        obj = {}
        stock = WereHouseStock.objects.filter(product_id = product_id, werehouse_id = request.user.profileuser.warehouse.id)
        print (stock)
        for ob in stock:
            print (ob)
            obj['stock'] = ob.stock
        return HttpResponse(json.dumps (obj), content_type='application/json')
        
@login_required
def gettypemovement(request,typemovement_id):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        res = []
        obj = {}
        warehouseconcept = WareHouseConcept.objects.filter(typemovement_id = typemovement_id)
        typemovement = TypeMovement.objects.filter(pk=typemovement_id)
        for c in warehouseconcept:
            obj[c.id] = c.title
            
        for b in typemovement:
            obj['typemovement'] = b.addition

        return HttpResponse(json.dumps (obj), content_type='application/json')

@login_required
def edittypemovement(request, typemovement_id):
    if request.method ==  'GET':
        
        typemovement =  get_object_or_404(TypeMovement,pk=typemovement_id, visible=True)
        form = AddTypeMovement(instance=typemovement)
        return render(request, 'edittypemovement.html', {
            'form':form
        })
    else :
        try: 
            typemovement =  get_object_or_404(TypeMovement,pk=typemovement_id, visible=True)
            form = AddTypeMovement(request.POST,instance=typemovement)
            form.save()
            messages.success(request,"Tipo de movimiento editado satisfactoriamente")
            return HttpResponseRedirect('/addtypemovement/')
        
        except ValueError:
            messages.success(request,"Error al actualizar el campo ")
            return HttpResponseRedirect('/addtypemovement/') 
@login_required      
def deletetypemovement(request, typemovement_id):
    
    try:
        typemovement =  get_object_or_404(TypeMovement,pk=typemovement_id, visible=True)
        typemovement.visible = False
        typemovement.save()
        messages.success(request,"Tipo de movimiento eliminado satisfactoriamente")
        return HttpResponseRedirect('/addtypemovement/')
        
    except ValueError:
        messages.success(request,"Error al actualizar el campo ")
        return HttpResponseRedirect('/addtypemovement/')
@login_required
def addwerehouseconcept(request):
    if request.method ==  'GET':
        warehouseconcept = WareHouseConcept.objects.filter(visible=True)
        return render(request, 'addwerehouseconcept.html', {
            'warehouseconcept': warehouseconcept,
            'form': AddWareHouseConcept
         })
    else:
        form = AddWareHouseConcept(request.POST)
        if (form.is_valid()):
            newwarehouseconcept =  form.save(commit=False)
            newwarehouseconcept.save()
            messages.success(request,"Concepto de Almacen creado satisfactoriamente")
            return HttpResponseRedirect('')
        else:
            messages.error(request,"Error en el formulario / revise los datos de registro")
            return HttpResponseRedirect('')   
@login_required       
def editwerehouseconcept(request, werehouseconcept_id):    
    if request.method ==  'GET':
        
        werehouseconcept =  get_object_or_404(WareHouseConcept,pk=werehouseconcept_id, visible=True)
        form = AddWareHouseConcept(instance=werehouseconcept)
        return render(request, 'editwerehouseconcept.html', {
            'form':form,
        })
    else :
        try: 
            werehouseconcept =  get_object_or_404(WareHouseConcept,pk=werehouseconcept_id, visible=True)
            form = AddWareHouseConcept(request.POST,instance=werehouseconcept)
            form.save()
            messages.success(request,"Concepto de almacén editado satisfactoriamente")
            return HttpResponseRedirect('/addwerehouseconcept/')
        
        except ValueError:
            messages.success(request,"Error al actualizar el campo ")
            return HttpResponseRedirect('/addwerehouseconcept/')
@login_required
def deletewerehouseconcept(request, werehouseconcept_id):
    try:
        werehouseconcept =  get_object_or_404(WareHouseConcept,pk=werehouseconcept_id, visible=True)
        werehouseconcept.visible = False
        werehouseconcept.save()
        messages.success(request,"Concepto de almacén eliminado satisfactoriamente")
        return HttpResponseRedirect('/addwerehouseconcept/')
        
    except ValueError:
        messages.success(request,"Error al actualizar el campo ")
        return HttpResponseRedirect('/addwerehouseconcept/') 
    
@login_required 
def addmovementwerehouse(request):
    if request.method ==  'GET':
        productswarehouse = WereHouseStock.objects.filter(werehouse_id = request.user.profileuser.warehouse_id)
        movements = WereHouseMovement.objects.filter(werehouse_id = request.user.profileuser.warehouse.id)
        return render(request, 'addmovementwerehouse.html', {
            
            'formtypemovement': AddWareHouseConcept,
            'products': productswarehouse,
            'movements': movements
         })
    else:
        try:
            #insertando en la cabecera de movimientos
            werehousemovement = WereHouseMovement.objects.create(typemovement_id = request.POST.get('typemovement') ,werehouseconcept_id = request.POST.get('concept'), werehouse_id = request.user.profileuser.warehouse.id,usercreated_id = request.user.id, observations = request.POST.get('observation'))
            werehousemovement .save()
            #insertando en el detalle de movimientos
            idmovement = WereHouseMovement.objects.last().id
            for key, value in request.POST.lists():
                    
                if key not in ('csrfmiddlewaretoken','typemovement','concept','observation', 'valuetypeMovement'):
                    
                    product = key.split('-')
                    canpd = "".join(value)
                    if(canpd>str(0)):
                       
                        detailsmovement = WereHouseMovementDetails.objects.create(canmov = canpd, product_id = product[0], usercreated_id = request.user.id,  werehousemovement_id = idmovement)
                                                                             
                        detailsmovement.save()
                        
                        #modificando el stock
                        if(request.POST.get('valuetypeMovement') ==  "resta"):
                            stock = WereHouseStock.objects.get(werehouse_id = request.user.profileuser.warehouse.id, product_id = product[0])
                            stock.stock = stock.stock - int (canpd) 
                            stock.save()
                        else:
                        #sumando
                            stock = WereHouseStock.objects.get(werehouse_id = request.user.profileuser.warehouse.id, product_id = product[0])
                            stock.stock = stock.stock + int(canpd) 
                            stock.save()
                        
            messages.success(request,"Movimiento de almacén generado exitosamente")
            return HttpResponseRedirect('/addmovementwerehouse/')
        except ValueError as ex :
            messages.success(request,ex)
            return HttpResponseRedirect('/addmovementwerehouse/')
        
@login_required       

def showreportmovements(request, werehousemovement_id):
    
    context = {'user': User.objects.filter(pk=request.user.id), 'movementsdetails': WereHouseMovementDetails.objects.filter(werehousemovement_id = werehousemovement_id),
               'movements':get_object_or_404(WereHouseMovement,pk=werehousemovement_id), 'totales': WereHouseMovementDetails.objects.filter(werehousemovement_id = werehousemovement_id).aggregate(Sum('canmov'))}
    
     # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template('core/reportmovements.html')
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

@login_required 

def addwerehousepurchasing(request):
    if request.method ==  'GET':
       
        listprice =  ProductList.objects.all()
        products = WereHouseStock.objects.filter(werehouse_id  = request.user.profileuser.warehouse.id)
        purchasing = WereHousePurchasing.objects.all()
        return render(request, 'addwerehousepurchasing.html', {
            
            'listprice': listprice,
            'products' : products,
            'purchasing': purchasing
         })
    else:
        
        print (request.POST)
        #insertando en la cabecera de compras
        WereHousePurchasing.objects.create(fecrem = request.POST.get('dateRemission'), totcom = request.POST.get('totaltotal'), observations = request.POST.get('observation'), usercreated_id = request.user.id)        
        
         #insertando en la cabecera de almacen
        
        WereHouseMovement.objects.create(typemovement_id = 1 ,werehouseconcept_id = 2, werehouse_id = request.user.profileuser.warehouse.id,usercreated_id = request.user.id, observations = request.POST.get('observation'))
        #insertando en el detalle cabecera de compras
    
        quantity  = request.POST.getlist("quantity")
        totcom = request.POST.getlist("total")
        predlp =  request.POST.getlist("predlp")
        productscom = request.POST.getlist("product")
        # id de compra insertada
        idcomp = WereHousePurchasing.objects.last().id
        
        #id del movimiento insertado
        idmov  = WereHouseMovement.objects.last().id
        for i in range(0,len(quantity)):
            #insertando en el detalle de la compra
            WereHousePurchasingDetails.objects.create(candco = quantity[i], totdco = totcom[i], predco = predlp[i], product_id = productscom[i],werehousepurchasing_id = idcomp )
            #insertando en el detalle del movimiento
            WereHouseMovementDetails.objects.create(canmov = quantity[i], product_id = productscom[i], usercreated_id = request.user.id,  werehousemovement_id = idmov)
            # afectando  entrada (suma) al almacen
            stock = WereHouseStock.objects.get(werehouse_id = request.user.profileuser.warehouse.id, product_id =productscom[i])
            stock.stock = stock.stock + int(quantity[i]) 
            stock.save()       
        
        
        messages.success(request,"Compra Generada Exitosamente")
        return HttpResponseRedirect('/addwerehousepurchasing/')
    

@login_required       

def showreportpurchasing(request, werehousepurchasings_id):
    
    context = {'user': User.objects.get(pk=request.user.id),
               'purchase':get_object_or_404(WereHousePurchasing,pk=werehousepurchasings_id),
               'detailspurchase': WereHousePurchasingDetails.objects.filter(werehousepurchasing_id =werehousepurchasings_id ),
               'totales': WereHousePurchasingDetails.objects.filter(werehousepurchasing_id = werehousepurchasings_id).aggregate(Sum('candco'),Sum('predco') )}
    
     # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report-purchase.pdf"'
    # find the template and render it.
    template = get_template('core/reportpurchasing.html')
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

@login_required

def addtransferwerehouse(request):
    if request.method ==  'GET':
        typemovementent = TypeMovement.objects.filter(visible=True, addition = True)
        tyypemovementsal = TypeMovement.objects.filter(visible=True, addition = False)
        warehouses = WareHouses.objects.filter(visible = True).exclude(pk=request.user.profileuser.warehouse.id)
        productswarehouse = WereHouseStock.objects.filter(werehouse_id = request.user.profileuser.warehouse_id)
        print ( warehouses)
        return render(request, 'addtransferwerehouse.html', 
                      {'moventrada':typemovementent, 'movsalida':tyypemovementsal,
                      'warehouses': warehouses, 'products': productswarehouse})
    else:
        try:
            #insertando en la cabecera de movimientos almacen de envio
            WereHouseMovement.objects.create(typemovement_id = request.POST.get('werehouseTypeMovementSend') ,werehouseconcept_id = request.POST.get('werehouseConceptSend'), werehouse_id = request.user.profileuser.warehouse.id,usercreated_id = request.user.id, observations = "SIN OBSERVACION")
            #insertando en la cabecera de movimientos almacen de recepcion
            WereHouseMovement.objects.create(typemovement_id = request.POST.get('werehouseTypeMovementReception') ,werehouseconcept_id = request.POST.get('werehouseConceptReception'), werehouse_id = request.POST.get('werehouseReception'),usercreated_id = request.user.id, observations = "SIN OBSERVACION")
            
            #insertando en el detalle de movimientos almacen envio  y recepcion
            idmovement = WereHouseMovement.objects.last().id
            for key, value in request.POST.lists():
                    
                if key not in ('csrfmiddlewaretoken','typeMovementSend','werehouseTypeMovementSend','werehouseConceptSend', 
                               'typeMovementReception','werehouseTypeMovementReception','werehouseConceptReception',
                               'werehouseReception'):
                    
                    product = key.split('-')
                    canpd = "".join(value)
                    if(canpd>str(0)):
                       
                        #detalle almacen de envio
                        WereHouseMovementDetails.objects.create(canmov = canpd, product_id = product[0], usercreated_id = request.user.id,  werehousemovement_id = idmovement-1)
                        #detalle almacen de recepcion
                        WereHouseMovementDetails.objects.create(canmov = canpd, product_id = product[0], usercreated_id = request.user.id,  werehousemovement_id = idmovement)
                        
                                                            
                        #modificando el stock almacen de envio
                       
                        stock = WereHouseStock.objects.get(werehouse_id = request.user.profileuser.warehouse.id, product_id = product[0])
                        stock.stock = stock.stock - int (canpd) 
                        stock.save()
                        
                        #modificando el stock del almacen de repcion

                        if(stockproduct(product[0],request.POST.get('werehouseReception'))):
                            
                            stock = WereHouseStock.objects.get(werehouse_id = request.POST.get('werehouseReception'), product_id = product[0])
                            stock.stock = stock.stock + int(canpd) 
                            stock.save()
                        else:
                            WereHouseStock.objects.create(werehouse_id = request.POST.get('werehouseReception'), stock = int(canpd) ,product_id = product[0] )
                        
            messages.success(request,"Transferencia de almacén generado exitosamente")
            return HttpResponseRedirect('/addtransferwerehouse/')

        except ValueError as ex :
            messages.success(request,ex)
        return HttpResponseRedirect('/addtransferwerehouse/')
