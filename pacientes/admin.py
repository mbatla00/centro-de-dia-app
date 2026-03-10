from django.contrib import admin
from .models import Paciente, ContactoEmergencia

class ContactoEmergenciaInline(admin.TabularInline):
    model = ContactoEmergencia
    extra = 1  # muestra 1 formulario vacío para añadir contacto

class PacienteAdmin(admin.ModelAdmin):
    inlines = [ContactoEmergenciaInline]
    list_display = ['nombre', 'apellidos', 'telefono']

admin.site.register(Paciente, PacienteAdmin)