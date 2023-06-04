from django import forms
from .models import Registrado

class RegModelForm(forms.ModelForm):
    class Meta:
        model = Registrado
        fields = ["nombre","apellido","email"]

    def clean_email(self):
        email = self.cleaned_data.get ("email")
        
        return "email@email.com"

class RegForm(forms.Form):
    nombre= forms.CharField(max_length=100)
    email = forms.EmailField()
    apellido = forms.CharField(max_length=100)
    