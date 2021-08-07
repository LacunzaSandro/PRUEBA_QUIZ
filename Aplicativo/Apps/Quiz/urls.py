from django.urls import path
from .views import (
    inicio,
    register,
    ingresar,
    salir,
    HomeUser,
    playQuiz,
    resultado_pregunta,
    scoreUsers)

urlpatterns = [
    path('', inicio, name='inicio'),
    path('homeusuario/', HomeUser, name='homeusuario'),

    path('register/', register, name='register'),
    path('login/', ingresar, name='login'),
    path('logout/', salir, name='logout'),

    path('playquiz/', playQuiz, name='playquiz'),
    path('resultado/<int:pregunta_respondida_pk>/',
         resultado_pregunta, name='resultado'),
    path('score/', scoreUsers, name='score'),
]
