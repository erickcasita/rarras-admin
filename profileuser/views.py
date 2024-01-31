from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
# Create your views here.
def signin (request):
    
    if request.method ==  'GET' and  not request.user.is_authenticated:
      
        return render(request, 'signup.html', {
            'form': AuthenticationForm
         })
    if  request.method ==  'GET' and  request.user.is_authenticated:
         return HttpResponseRedirect('/dashboard')
     
    if  request.method ==  'POST':
        user = authenticate(request, username= request.POST['username'], password=request.POST['password'])
        if user is None:
            messages.success(request,"Usuario y / o Passwords incorrectos")
            return HttpResponseRedirect('')
        else:
            login(request, user)
            return HttpResponseRedirect('/dashboard/')
def signout(request):
    logout(request)
    return HttpResponseRedirect('/signin/')
    