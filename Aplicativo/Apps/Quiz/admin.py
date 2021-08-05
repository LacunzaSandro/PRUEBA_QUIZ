import django
from django.contrib import admin
from django.db import models
from django.db.models.base import Model


# Register your models here.
from .models import Pregunta, ElegirRespuesta, PreguntasRespondidas
from .forms import ElegirInLineFormSet

# mejoramos como se ve en sección admin


class ElegirRespuestaInline(admin.TabularInline):
    model = ElegirRespuesta
    can_delete = False
    max_num = ElegirRespuesta.MAX_RESPONSE
    min_num = ElegirRespuesta.MAX_RESPONSE
    formset = ElegirInLineFormSet


class PreguntaAdmin(admin.ModelAdmin):
    model = Pregunta
    inlines = (ElegirRespuestaInline,)
    list_display = ['texto', ]
    search_fields = ['texto', 'preguntas__texto']  # dos niveles arriba


class PreguntasRespondidasAdmin(admin.ModelAdmin):
    list_display = ['pregunta', 'respuesta', 'correcto', 'puntaje_obtenido']

    class Metal:
        model = PreguntasRespondidas


# registramos en secciones admin
admin.site.register(PreguntasRespondidas)
admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(ElegirRespuesta)
