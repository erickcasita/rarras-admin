"""
URL configuration for rarrasadmin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from warehouses import views
from products import views as pd
from profileuser import views as pusr
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('profileuser.urls')),
    path('', include('warehouses.urls')),
    path('', include('products.urls')),
    path('', include('reports.urls')),
    path('', include('home.urls')),
]
