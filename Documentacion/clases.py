class Usuario:
    def __init__(self,nombre,appellido,edad,genero,interes,bio,limiteDis,locacion,rangoEdad):
        self.nombre =nombre
        self.apellido=appellido
        self.edad=edad
        self.genero=genero
        self.interes=interes
        self.bio=bio
        self.limiteDis=limiteDis
        self.locacion=locacion
        self.rangoEdad=rangoEdad
        

class locacion:
    def __init__(self,calle,direccion,barrio,provincia,ciudad,pais):
        self.calle=calle
        self.direccion=direccion
        self.barrio=barrio
        self.provincia=provincia
        self.ciudad=ciudad
        self.pais=pais
        
class like:
    def __init__(self,listLikes,listDislikes):
        self.listLikes=listLikes
        self.listDislikes=listDislikes
        

class superlike:
    def __init__(self,listaSuperlike) -> None:
        self.listaSuperlike=listaSuperlike
        
class match:
    def __init__(self,chat,likes,superlikes,bloqueados) -> None:
        self.chat=chat
        self.likes=likes
        self.superlikes=superlikes
        self.bloqueados=bloqueados
        
class chats:
    def __init__(self,mensajes,userReport,multimedia,listContactos):
        self.mensajes=mensajes
        self.userReport=userReport
        self.multimedia=multimedia
        self.listContactos=listContactos
        
class unmatch:
    def __init__(self,listaUnmatch,causa,bloqueos,reportes):
        self.listaUnmatch=listaUnmatch
        self.causa=causa
        self.bloqueos=bloqueos
        self.reportes=reportes
        
        
        
        
        