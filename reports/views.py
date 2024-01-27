from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from products.models import Categories
from warehouses.models import WareHouses

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
        pass

@login_required
def reportmovement (request):
    if request.method ==  'GET':
        return render(request, 'reportmovement.html')
    else:
        pass