from django.contrib import admin
from .models import Usuario,Locacion,unmatch,Match,Likeados,Planes,Mensajes

class Usuarioad(admin.ModelAdmin):
    list_display =("id_usuario", "nombres","apellido" , "edad" , "genero" , "interes" ,"bio_personal" ,"limite_distancia", "rango_edad")
class Locacionad(admin.ModelAdmin):
    list_display =("id_locacion" , "id_usuario" , "nombre_calle" , "numero_direccion" , "barrio" , "provincia" ,  "ciudad" , "pais" )
class Unmatchad(admin.ModelAdmin):
    list_display = ("id_usuario_bloqueado" ,"id_usuario" , "causa")
class Matchad(admin.ModelAdmin):
    list_display = ("id_match" ,"id_usuario")
class Likeadosad(admin.ModelAdmin):
    list_display = ("id_like" , "id_usuario" , "lista_likes" , "lista_dilikes")
class Planesad(admin.ModelAdmin):
    list_display = ("id_premiun" ,"id_usuario" ,"tipo_plan" ,"metodo_pago")
class Mensajesad(admin.ModelAdmin):
    list_display = ("chat_id" ,"id_usuario2" ,"contenido") 

admin.site.register(Usuario , Usuarioad)

admin.site.register(Locacion , Locacionad)

admin.site.register(unmatch , Unmatchad)

admin.site.register(Match, Matchad )

admin.site.register(Likeados , Likeadosad)

admin.site.register(Planes , Planesad)

admin.site.register(Mensajes , Mensajesad)



