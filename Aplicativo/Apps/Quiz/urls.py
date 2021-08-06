from django.urls import path
from .views import inicio, register, ingresar, salir, HomeUser

urlpatterns = [
    path('', inicio, name='inicio'),
    path('homeusuario/', HomeUser, name='homeusuario'),

    path('register/', register, name='register'),
    path('login/', ingresar, name='login'),
    path('logout/', salir, name='logout'),

]
