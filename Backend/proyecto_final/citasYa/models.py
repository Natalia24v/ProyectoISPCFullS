from django.db import models


# datos del usuario 1
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.CharField(max_length=30)
    genero = models.CharField(max_length=30)
    interes = models.CharField(max_length=100)
    bio_personal = models.TextField(max_length=1000)
    limite_distancia = models.CharField(max_length=30)
    rango_edad = models.CharField(max_length=30)
    class Meta:
        db_table = "usuario"
        verbose_name = "Datos de usuario"
        verbose_name_plural = "Usuarios"
    def __unicode__(self):
        return self.nombres
    def __str__(self):
        return str(self.nombres)
    
    # Locacion del usuario 2
class Locacion(models.Model):
    id_locacion = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario , to_field="id_usuario", on_delete=models.CASCADE)
    nombre_calle = models.CharField(max_length=100)
    numero_direccion = models.CharField(max_length=10)
    barrio = models.CharField(max_length=10)
    provincia = models.CharField(max_length=10)
    ciudad = models.CharField(max_length=10)
    pais = models.CharField(max_length=10)

    class Meta:
        db_table = "locacion"
        verbose_name = "locacion de usuario"
        verbose_name_plural = "locaciones"
    def __unicode__(self):
        return self.id_locacion
    def __str__(self):
        return str(self.id_locacion)
    
    #    unmatch 3
class unmatch(models.Model):
    id_usuario_bloqueado = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario , to_field="id_usuario", on_delete=models.CASCADE)
    causa = models.CharField(max_length=1000)
    class Meta:
        db_table = "unmatch"
        verbose_name = "Lista de contactos rechazados"
        verbose_name_plural = "unmatches"
    def __unicode__(self):
        return self.id_usuario_bloqueado
    def __str__(self):
        return str(self.id_usuario_bloqueado)
    
# tabla de matches 4
class Match(models.Model):
    id_match = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario , to_field="id_usuario", on_delete=models.CASCADE)
    

    class Meta:
        db_table = "Match"
        verbose_name = "Usuario que hicieron match"
        verbose_name_plural = "Matchs"
    def __unicode__(self):
        return self.id_match
    def __str__(self):
        return str(self.id_match)

# usuarios likeados 5
class Likeados(models.Model):
    id_like = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario , to_field="id_usuario", on_delete=models.CASCADE)
    lista_likes = models.CharField(max_length=1000)
    lista_dilikes = models.CharField(max_length=1000)

    class Meta:
        db_table = "likeado"
        verbose_name = "Usuario likeados y dislikeados"
        verbose_name_plural = "likeados"
    def __unicode__(self):
        return self.id_like
    def __str__(self):
        return str(self.id_like)

# usuarios con planes a ofrecer 6
class Planes(models.Model):
    id_premiun = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario , to_field="id_usuario", on_delete=models.CASCADE)
    tipo_plan = models.CharField(max_length=100)
    metodo_pago = models.CharField(max_length=100)
    

    class Meta:
        db_table = "planes"
        verbose_name = "Usuarios premiun"
        verbose_name_plural = "planes"
    def __unicode__(self):
        return self.id_premiun
    def __str__(self):
        return str(self.id_premiun)
    
class Mensajes(models.Model):
    chat_id = models.AutoField(primary_key=True)
    id_usuario2 = models.ForeignKey(Usuario , to_field="id_usuario", on_delete=models.CASCADE)
    contenido = models.CharField(max_length=1000)
    class Meta:
        db_table = "mensaje"
        verbose_name = "chats de usuarios"
        verbose_name_plural = "mensajes"
    def __unicode__(self):
        return self.chat_id
    def __str__(self):
        return str(self.chat_id)