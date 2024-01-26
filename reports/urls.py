from django.urls import path
from . import views

urlpatterns = [
    path('reportstock/',views.reportstock, name='reportstock'),
]