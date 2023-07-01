from django.contrib import admin
from .forms import RegModelForm
from .models import Registrado


class AdminRegistrado(admin.ModelAdmin):
    list_display=["email", "nombre","apellido"]
    form = RegModelForm
    list_filter =["nombre"]
    list_editable = ["nombre"]
    search_fields = ["email" , "apellido"]
    # class Meta:
    #     model = Registrado

admin.site.register(Registrado,AdminRegistrado)
