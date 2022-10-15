from io import open_code
from django.db import models
from django_countries.fields import CountryField

# Create your models here.
class Director(models.Model):
    name = models.CharField(max_length=64, help_text="Poner nombre del director")
    surname = models.CharField(max_length=64, help_text="Poner nombre del director")
    birth = models.DateField(null=True, blank=True)
    nationality = CountryField()
    
    def __str__(self):
        return '%s %s' % (self.name, self.surname)
    
class Cast(models.Model):
    name = models.CharField(max_length=64, help_text="Poner nombre del actor, 'Nombre Apellido'")

    def __str__(self):
        return self.name

class Film(models.Model):
    name = models.CharField(max_length=64, help_text="Pone el nombre de la película")
    age = models.DateField(null=True, blank=True, help_text="Pon la fecha de lanzamiento de la película")
    genero = models.CharField(max_length=50, help_text="Pon el género de la película")
    cast = models.ManyToManyField(Cast)
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(help_text="Pon un resumen de la película")
    
    def __str__(self):
        return self.name