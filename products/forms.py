from django import forms
from .models import Categories,Brands,Products,ProductList

class  AddCategories (forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddCategories, self).__init__(*args, **kwargs)
        # desde aquí, puedes definir luego de iniciar el formulario, si los campos son obligatorios
        self.fields['name'].required = True, # así no entrara al save(), si el campo no está lleno
        self.fields['sat'].required = True,
        self.fields['umedida'].required = True,
        
    
    def clean_name(self):
        return self.cleaned_data["name"].upper()
    def clean_umedida(self):
        return self.cleaned_data["umedida"].upper()

    class Meta:
        model = Categories
        fields = ['name','sat','umedida']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'nameValidation'
            }),
            
             'sat': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'sat',
                'type': 'number'
            }),
             
            'umedida': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'umedida'
                
            }),
        }
class AddBrands (forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(AddBrands, self).__init__(*args, **kwargs)
        # desde aquí, puedes definir luego de iniciar el formulario, si los campos son obligatorios
        self.fields['name'].required = True, # así no entrara al save(), si el campo no está lleno
        self.fields['categories'].required = True,
        
        
    
    def clean_name(self):
        return self.cleaned_data["name"].upper()


    class Meta:
        model = Brands
        fields = ['name','categories']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'nameValidation'
            }),
            
             'categories': forms.Select(attrs={
                'class': 'form-select',
                'id': 'branchValidations'
            }),
             
        }   
        
class AddProducts (forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(AddProducts, self).__init__(*args, **kwargs)
        # desde aquí, puedes definir luego de iniciar el formulario, si los campos son obligatorios
        self.fields['name'].required = True, # así no entrara al save(), si el campo no está lleno
        self.fields['categories'].required = True,
        self.fields['brands'].required = True,
        self.fields['cvesap'].required = True,
        
    
    def clean_name(self):
        return self.cleaned_data["name"].upper()


    class Meta:
        model = Products
        fields = ['name','categories','brands','cvesap']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'nameValidation'
            }),
            
             'categories': forms.Select(attrs={
                'class': 'form-select',
                'id': 'branchValidations'
            }),
             
            'brands': forms.Select(attrs={
                'class': 'form-select',
                'id': 'branchValidations2'
            }),
            
            'cvesap': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'cvesap',
                'type' : 'number'
            }),
             
        }   
        
class AddProductList(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddProductList, self).__init__(*args, **kwargs)
        # desde aquí, puedes definir luego de iniciar el formulario, si los campos son obligatorios
        self.fields['name'].required = True, # así no entrara al save(), si el campo no está lleno

        
    
    def clean_name(self):
        return self.cleaned_data["name"].upper()


    class Meta:
        model = ProductList
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                
            }),
                 
        }   
        