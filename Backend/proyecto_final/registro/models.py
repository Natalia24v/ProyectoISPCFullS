from __future__ import unicode_literals
from django.db import models




class Registrado(models.Model):
    
    nombre = models.CharField(max_length=100 , blank=True , null=False)
    apellido = models.CharField(max_length=100 , blank=True , null=False)
    email =models.EmailField()
    

    def __unicode__(self):
        return self.email
    
    def __str__(self):
        return self.email
