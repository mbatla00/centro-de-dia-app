from django.db import models

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=150)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.CharField(max_length=200, blank=True)

    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"
    
class ContactoEmergencia(models.Model):
    paciente = models.ForeignKey(
        Paciente, 
        on_delete=models.CASCADE,
        related_name='contactos'
    )
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    relacion = models.CharField(max_length=50)  # ej: hijo, hermana, cuidador
    
    def __str__(self):
        return f"{self.nombre} - {self.relacion} de {self.paciente.nombre}"