from django.shortcuts import redirect, render
from .forms import RegisterForm
# Create your views here.


def inicio(request):
    context = {
        'bienvenido': 'Bienvenido'
    }
    return render(request, 'inicio.html', context)


def register(request):
    titulo = 'Crea una cuenta'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RegisterForm()
    context = {
        'form': form,
        'titulo': titulo,
    }
    return render(request, 'Usuario/register.html', context)
