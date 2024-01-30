from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from products.models import Categories
from warehouses.models import WareHouses,WereHouseStock, WereHouseMovementDetails, WareHouseConcept,TypeMovement
from products.models import Categories
from django.db.models import Sum
from django.contrib import messages
from django.contrib.auth.models import User
from datetime import datetime
from warehouses.forms import AddWareHouseConcept
#reports
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
# Create your views here.

@login_required
def reportstock (request):
    if request.method ==  'GET':
        categories = Categories.objects.filter(visible=True)
        werehouses = WareHouses.objects.filter(visible=True)
        return render(request, 'reportstock.html', {
            'categories': categories,
            'werehouses': werehouses
        })
    else:
        idwerehouse = request.POST.get('werehouse')
        idcategory = request.POST.get('categories')
        user = request.user.username
        datenow = datetime.now()
        stock = WereHouseStock.objects.filter(werehouse_id = idwerehouse, product__categories_id = idcategory)
        werehouse = WareHouses.objects.get(visible=True, pk = idwerehouse)
        category = Categories.objects.get(visible = True , pk = idcategory)
        totales = WereHouseStock.objects.filter(werehouse_id = idwerehouse, product__categories_id = idcategory).aggregate(Sum('stock'))
        context = {'user': user ,'stock' : stock, 'werehouse':werehouse, 'category': category,
                   'totales':totales, 'datenow': datenow}
    
        # Create a Django response object, and specify content_type as pdf
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="report.pdf"'
        # find the template and render it.
        template = get_template('core/reportstock.html')
        html = template.render(context)

        # create a pdf
        pisa_status = pisa.CreatePDF(
        html, dest=response)
        # if error then show some funny view
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response
    
@login_required
def reportmovement (request):
    if request.method ==  'GET':
        werehouses = WareHouses.objects.filter(visible=True)
        return render(request, 'reportmovement.html', {
            'werehouses': werehouses,
            'formtypemovement': AddWareHouseConcept,
        })
    else:
        concepid = request.POST.get('concept')
        typemovement = request.POST.get('typemovement')
        idwerehouse = request.POST.get('werehouse')
        initdate = request.POST.get('date_init')
        finaldate = request.POST.get('date_finish')
        user = request.user.username
        datenow = datetime.now()
        movement = WereHouseMovementDetails.objects.all().filter(werehousemovement__created__range=(initdate, finaldate), 
                                                                 werehousemovement__werehouseconcept_id = concepid,
                                                                 werehousemovement__typemovement_id = typemovement)
        totales = WereHouseMovementDetails.objects.all().filter(werehousemovement__created__range=(initdate, finaldate), 
                                                                 werehousemovement__werehouseconcept_id = concepid,
                                                                 werehousemovement__typemovement_id = typemovement).aggregate(Sum('canmov'))
        
        #test = WereHouseMovementDetails.objects.all().filter(werehousemovement__created__range=(initdate, finaldate), 
        #                                                        werehousemovement__typemovement_id = typemovement)
        concept = WareHouseConcept.objects.get(visible = True , pk = concepid)
        tmovement = TypeMovement.objects.get(visible = True , pk = typemovement)
        werehouses = WareHouses.objects.get(visible = True , pk = idwerehouse)
        #folios = [20,24,25,26]
        #print(i.werehousemovement.id , i.werehousemovement.typemovement.name, i.werehousemovement.werehouseconcept.title, i.product.name, i.canmov)
        context = {'movement': movement, 'concept': concept, 'tmovement': tmovement, 'werehouses': werehouses,
                   'initdate': initdate, 'finaldate': finaldate, 'user': user, 'datenow': datenow, 'totales': totales}
    
        # Create a Django response object, and specify content_type as pdf
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="report.pdf"'
        # find the template and render it.
        template = get_template('core/reportmovementsform.html')
        html = template.render(context)

        # create a pdf
        pisa_status = pisa.CreatePDF(
        html, dest=response)
        # if error then show some funny view
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response