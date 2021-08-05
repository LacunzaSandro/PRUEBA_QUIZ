from django.urls import path
from .views import inicio, register

urlpatterns = [
    path('', inicio, name='inicio'),
    path('register/', register, name='register'),
]
