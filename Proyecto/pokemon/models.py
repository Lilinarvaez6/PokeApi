from django.db import models

# Create your models here.
class Usuario(models.Model):
	nombre = models.CharField(max_length=250)
	edad = models.CharField(max_length=250)

class Pokemon(models.Model):
	nombre = models.CharField(max_length=250)
	tipo = models.CharField(max_length=250)

class Usu_poke(models.Model):
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)