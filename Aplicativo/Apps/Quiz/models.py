from django.db import models
from django.contrib.auth.models import User
# Modelo pregunta


class Pregunta(models.Model):
    RESPUESTAS_PERMITIDAS = 1
    texto = models.TextField(verbose_name='Texto de la pregunta')

    def __str__(self):
        return self.texto

# Relación Pregunta con posibles respuestas


class ElegirRespuesta(models.Model):
    MAX_RESPONSE = 5  # número para definir el número de respuestas posibles
    pregunta = models.ForeignKey(
        Pregunta, related_name='preguntas', on_delete=models.CASCADE)
    correcta = models.BooleanField(
        verbose_name='¿Es esta la respuesta correcta?', default=False, null=False)
    texto = models.TextField(verbose_name='Texto de la respuesta')

    def __str__(self):
        return self.texto


class Usuario(models.Model):
    # Usuario que esta realizando el Quiz
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    puntaje_total = models.DecimalField(
        verbose_name='Puntaje Total', default=0, decimal_places=2, max_digits=10)


class PreguntasRespondidas(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    respuesta = models.ForeignKey(
        ElegirRespuesta, on_delete=models.CASCADE, related_name='intentos')
    correcta = models.BooleanField(
        verbose_name='¿Es esta la respuesta correcta?', default=False, null=False)
    puntaje_obtenido = models.DecimalField(
        verbose_name='Puntaje obtenido', default=0, decimal_places=2, max_digits=6)
