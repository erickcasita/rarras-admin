from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def reportstock (request):
    if request.method ==  'GET':
        return render(request, 'reportstock.html')
    else:
        pass