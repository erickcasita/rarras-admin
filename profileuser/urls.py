from django.urls import path
from . import views as pusr
urlpatterns = [
    path('', pusr.signin, name='root'),
    path('signin/', pusr.signin, name='signin'),
    path('signout/', pusr.signout, name='signout'),

]