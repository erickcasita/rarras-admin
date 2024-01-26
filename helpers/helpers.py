from warehouses.models import WereHouseStock

def stockproduct(product_id,werehouse_id):
    stock =  WereHouseStock.objects.filter(product_id = product_id, werehouse_id = werehouse_id).exists()
    return stock