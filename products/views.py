from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .models import Categories,Brands,Products,ProductList,ProductListDetails
from warehouses.models import WareHouses,WereHouseStock
from .forms import AddCategories,AddBrands,AddProducts,AddProductList
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import json
# Create your views here.

@login_required
def addCategories (request):
    if request.method ==  'GET':
        categories = Categories.objects.filter(visible=True)
        return render(request, 'addcategories.html', {
            'form': AddCategories,
            'categories': categories 
         })
    else:
        form = AddCategories(request.POST)
        if (form.is_valid()):
            newcategories =  form.save(commit=False)
            newcategories.save()
            messages.success(request,"Categoría de productos creada correctamente")
            return HttpResponseRedirect('')
        else:
            messages.error(request,"Error en el formulario / revise los datos de registro")
            return HttpResponseRedirect('')
@login_required
    
def editCategories(request, categories_id):
    if request.method ==  'GET':
        
        categories =  get_object_or_404(Categories,pk=categories_id, visible=True)
        form = AddCategories(instance=categories)
        return render(request, 'editcategories.html', {
            'form':form
        })
    else :
        try:
            categories =  get_object_or_404(Categories,pk=categories_id, visible=True)
            form = AddCategories(request.POST,instance=categories)
            form.save()
            messages.success(request,"Categoría editada satisfactoriamente")
            return HttpResponseRedirect('/addcategories/')
        
        except ValueError:
            messages.success(request,"Error al actualizar el campo ")
            return HttpResponseRedirect('/addcategories/')
@login_required

def deleteCategories(request, categories_id):
    
    try:
        categories =  get_object_or_404(Categories,pk=categories_id, visible=True)
        categories.visible = False
        categories.save()
        messages.success(request,"Categoria eliminada satisfactoriamente")
        return HttpResponseRedirect('/addcategories/')
        
    except ValueError:
        messages.success(request,"Error al actualizar el campo ")
        return HttpResponseRedirect('/addwerehouse/')
@login_required

def addBrands (request):
    if request.method ==  'GET':
        brands = Brands.objects.filter(visible=True)
        return render(request, 'addbrands.html', {
            'form': AddBrands,
            'brands': brands 
         })
    else:
        form = AddBrands(request.POST)
        if (form.is_valid()):
            newbrands =  form.save(commit=False)
            newbrands.save()
            messages.success(request,"Marca de productos creada correctamente")
            return HttpResponseRedirect('')
        else:
            messages.error(request,"Error en el formulario / revise los datos de registro")
            return HttpResponseRedirect('') 
@login_required

def editBrands(request, brands_id):
    
    if request.method ==  'GET':
        
        brands =  get_object_or_404(Brands,pk=brands_id, visible=True)
        form = AddBrands(instance=brands)
        return render(request, 'editbrands.html', {
            'form':form
        })
    else :
        try:
            brands =  get_object_or_404(Brands,pk=brands_id, visible=True)
            form = AddBrands(request.POST,instance=brands)
            form.save()
            messages.success(request,"Marca de producto editada satisfactoriamente")
            return HttpResponseRedirect('/addbrands/')
        
        except ValueError:
            messages.success(request,"Error al actualizar el campo ")
            return HttpResponseRedirect('/addbrands/')
@login_required
        
def deletebrands(request, brands_id):
    try:
        brands =  get_object_or_404(Brands,pk=brands_id, visible=True)
        brands.visible = False
        brands.save()
        messages.success(request,"Marca de productos eliminada satisfactoriamente")
        return HttpResponseRedirect('/addbrands/')
        
    except ValueError:
        messages.success(request,"Error al actualizar el campo ")
        return HttpResponseRedirect('/addbrands/')

@login_required

def addProducts (request):
    if request.method ==  'GET':
        products = Products.objects.filter(visible=True)
        werehouses = WareHouses.objects.filter(visible=True)
        return render(request, 'addproducts.html', {
            'form': AddProducts,
            'products': products,
            'werehouses': werehouses
         })
    else:
        try:
            
            form = AddProducts(request.POST)
            if (form.is_valid()):
                
                newproducts =  form.save(commit=False)
                
                newproducts.save()
                
                idproduct = Products.objects.last().id
                werehouses =  request.POST.getlist('warehouse')
                for ware in werehouses:
                    stock = WereHouseStock.objects.create(werehouse_id = int(ware), stock = 0 ,product_id = idproduct )
                    stock .save()
                messages.success(request,"Producto creado correctamente")
                return HttpResponseRedirect('')
            else:
                messages.error(request,"Error en el formulario / revise los datos de registro")
                return HttpResponseRedirect('')
        except ValueError as e :
            messages.success(request, e)
            return HttpResponseRedirect('')
@login_required

def editproduct (request, products_id):

    if request.method ==  'GET':
        
        products =  get_object_or_404(Products,pk=products_id, visible=True)
        form = AddProducts(instance=products)
        return render(request, 'editproducts.html', {
            'form':form
        })
    else :
        try:
            products =  get_object_or_404(Products,pk=products_id, visible=True)
            form = AddProducts(request.POST,instance=products)
            form.save()
            messages.success(request,"Producto editado satisfactoriamente")
            return HttpResponseRedirect('/addproducts/')
        
        except ValueError:
            messages.success(request,"Error al actualizar el campo ")
            return HttpResponseRedirect('/addproducts/')
@login_required

def deleteproduct(request, products_id):
    try:
        #consultando si el producto se encuentra registrado en algun almacen
        
        countproducts = WereHouseStock.objects.filter(product_id = products_id, stock__gte=1).count()
        
        if (countproducts <=0):
            products =  get_object_or_404(Products,pk=products_id, visible=True)
            products.visible = False
            products.save()
            messages.success(request,"Productos eliminado satisfactoriamente")
            return HttpResponseRedirect('/addproducts/')
        messages.success(request,"El producto tiene existencia en un almacén / No se puede eliminar ")
        return HttpResponseRedirect('/addproducts/')
    except ValueError:
        messages.success(request,"Error al actualizar los campos")
        return HttpResponseRedirect('/addproducts/')
@login_required

def addProductList(request):
    if request.method ==  'GET':
        productslist = ProductList.objects.filter(visible=True)
        products = Products.objects.filter(visible=True)
        return render(request, 'addproductslist.html', {
            'form': AddProductList,
            'productslist': productslist,
            'products': products
         })
    else:
      
        try:
            form = AddProductList(request.POST)
            if (form.is_valid()):
                
                newproductslist =  form.save(commit=False)
                newproductslist.save()
                idproductlist = ProductList.objects.last().id
      
                for key, value in request.POST.lists():
                    
                    if key not in ('csrfmiddlewaretoken','name','products'):
                        product = key[7:]
                        price = "".join(value)
                        productlistdetails = ProductListDetails.objects.create(productlist_id = int(idproductlist),product_id = int (product), predlp = float(price))
                        productlistdetails .save()
               
        
                messages.success(request,"Lista de precios creada correctamente")
                return HttpResponseRedirect('')
            else:
                messages.error(request,"Error en el formulario / revise los datos de registro")
                return HttpResponseRedirect('')   
        
        except ValueError as e :
            messages.success(request, e)
            return HttpResponseRedirect('') 

@login_required

def editproductslist(request, productlist_id):
    if request.method ==  'GET':
        
        products =   Products.objects.filter(visible=True)
        productslist =  get_object_or_404(ProductList,visible=True, pk=productlist_id) 
        form = AddProductList(instance = productslist)
        productlistdetails = ProductListDetails.objects.filter(productlist_id=productlist_id)
        
        return render(request, 'editproductslist.html', {
            'form': form,
            'products':products,
            'productlistdetails':productlistdetails
        })
    else :
        try:
            productslist =  get_object_or_404(ProductList,pk=productlist_id, visible=True)
            form = AddProductList(request.POST,instance=productslist)
            form.save()
            
            # eliminando el contanido de la lista de precios
            
            deleteproductlist = ProductListDetails.objects.filter(productlist_id=productlist_id)
            deleteproductlist.delete()
            
            # insertando nuevos elementos
            
            for key, value in request.POST.lists():
                    
                if key not in ('csrfmiddlewaretoken','name','products'):
                    
                    product = key[7:]
                    price = "".join(value)
                    productlistdetails = ProductListDetails.objects.create(productlist_id = int(productlist_id),product_id = int (product), predlp = float(price))
                    productlistdetails .save()
            
            messages.success(request,"Lista de precios editada satisfactoriamente")
            return HttpResponseRedirect('/addproductslist/')
        
        except ValueError:
            messages.success(request,"Error al actualizar el campo ")
            return HttpResponseRedirect('/addproductslist/')
        

@login_required

def getpriceproduct(request, product_id):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        obj = {}
        price = ProductListDetails.objects.filter(product_id = product_id, productlist_id = request.POST.get('productlist'))
        print(price)
        for ob in price:
            print (ob)
            obj['predlp'] = ob.predlp
            obj['cvesap'] = ob.product.cvesap
        return HttpResponse(json.dumps (obj), content_type='application/json')