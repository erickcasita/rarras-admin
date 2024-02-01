from django import forms
from .models import WareHouses,TypeMovement,WareHouseConcept
class  AddWareHouse (forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddWareHouse, self).__init__(*args, **kwargs)
        # desde aquí, puedes definir luego de iniciar el formulario, si los campos son obligatorios
        self.fields['title'].required = True, # así no entrara al save(), si el campo no está lleno
        self.fields['store'].required = True,
    
    def clean_title(self):
        return self.cleaned_data["title"].upper()

    class Meta:
        model = WareHouses
        fields = ['title','store']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'nameValidation'
            }),
            
             'store': forms.Select(attrs={
                'class': 'form-select',
                'id': 'branchValidation'
            }),
        }
class AddTypeMovement (forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(AddTypeMovement, self).__init__(*args, **kwargs)
        # desde aquí, puedes definir luego de iniciar el formulario, si los campos son obligatorios
        self.fields['name'].required = True,# así no entrara al save(), si el campo no está lleno     
    def clean_name(self):
        return self.cleaned_data["name"].upper()

    class Meta:
        model = TypeMovement
        fields = ['name','addition']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'nameValidation'
            }),
            'addition': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'id': 'checkaddition'
            }),
        }
    
class  AddWareHouseConcept (forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddWareHouseConcept, self).__init__(*args, **kwargs)
        # desde aquí, puedes definir luego de iniciar el formulario, si los campos son obligatorios
        self.fields['title'].required = True, # así no entrara al save(), si el campo no está lleno
        self.fields['typemovement'].queryset = TypeMovement.objects.filter(visible = True)
        self.fields['typemovement'].required = True
        self.fields['description'].required = True,
    
    def clean_title(self):
        return self.cleaned_data["title"].upper()
    
    def clean_description(self):
        return self.cleaned_data["description"].upper()

    class Meta:
        model = WareHouseConcept
        fields = ['title','typemovement','description']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'nameValidation'
            }),
            
             'typemovement': forms.Select(attrs={
                'class': 'form-select',
                'id': 'branchValidation'                
            }),
             
                'description': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'descriptionValidation',
                'rows': '2',
                'cols': '0' 
            }), 
        }
   
