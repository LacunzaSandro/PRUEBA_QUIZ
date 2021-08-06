from django.contrib.auth import authenticate
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout 
from .models import QuizUsuario
from .forms import RegisterForm, UsuarioLoginForm
# Create your views here.

#Index
def inicio(request):
    context = {
        'bienvenido': 'Bienvenido'
    }
    return render(request, 'inicio.html', context)

#Register 
def register(request):
    titulo = 'Crea una cuenta'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    context = {
        'form': form,
        'titulo': titulo,
    }
    return render(request, 'Usuario/register.html', context)

#Home's User
def HomeUser(request):
    return render(request, 'Usuario/home.html')

#Login
def ingresar(request):
    titulo = 'Login'
    form = UsuarioLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        usuario = authenticate(username=username, password= password)
        login(request, usuario)
        return redirect('/homeusuario')

    context = {
        'form': form,
        'titulo': titulo
    }

    return render(request, 'Usuario/login.html', context)
#Logout
def salir(request):
    logout(request)
    return redirect('/')

def playQuiz(request):
    QuizUsuario, created = QuizUsuario.objects.get_or_create(usuario=request.user)
