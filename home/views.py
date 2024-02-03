from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from products.models import Products
from store.models import Store
from warehouses.models import WareHouses, WereHouseStock
from django.db.models import Sum,F

# Create your views here.
@login_required
def dashboard (request):
    if request.method ==  'GET':
        products = Products.objects.filter(visible=True).count()
        stores = Store.objects.count()
        werehouses = WareHouses.objects.filter(visible=True).count()
        werehouseStock = WereHouseStock.objects.values('werehouse').annotate(stock=Sum('stock'), title=F('werehouse__title')).annotate().order_by('werehouse')
        return render(request, 'dashboard.html',
            {
                'products': products,
                'stores': stores,
                'werehouses': werehouses,
                'werehouseStock': werehouseStock
            })
    else:
        pass