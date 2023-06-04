from django.shortcuts import render

from .forms import RegForm
from .models import Registrado

def inicio(request):
    form = RegForm(request.POST or None)
    if form.is_valid():
        form_data =form.cleaned_data
        abc= form_data.get("email")
        abc2= form_data.get("nombre")
        abc3 = form_data.get("apellido")
        obj = Registrado.objects.create(email=abc, nombre=abc2 ,apellido=abc3)
        
    context = {
        "el_form" : form,
    }
    return render(request,"inicio.html",context)
