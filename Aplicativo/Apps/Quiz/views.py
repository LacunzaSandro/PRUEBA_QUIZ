from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.http import request
from django.http.response import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login, logout
from .models import QuizUsuario, Pregunta, PreguntasRespondidas
from .forms import RegisterForm, UsuarioLoginForm
# Create your views here.

# Index


def inicio(request):
    context = {
        'bienvenido': 'Bienvenido'
    }
    return render(request, 'inicio.html', context)

# Register


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

# Home's User


def HomeUser(request):
    return render(request, 'Usuario/home.html')


def scoreUsers(request):
    # definimos que solo se mostraran los diez primeros de la lista
    total_user_quiz = QuizUsuario.objects.order_by('-puntaje_total')[:10]
    contador = total_user_quiz.count()

    context = {
        'usuario_quiz': total_user_quiz,
        'contar_user': contador
    }
    return render(request, 'Play/score.html', context)

# Login


def ingresar(request):
    titulo = 'Login'
    form = UsuarioLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        usuario = authenticate(username=username, password=password)
        login(request, usuario)
        return redirect('/homeusuario')

    context = {
        'form': form,
        'titulo': titulo
    }

    return render(request, 'Usuario/login.html', context)
# Logout


def salir(request):
    logout(request)
    return redirect('/')


def playQuiz(request):
    QuizUser, created = QuizUsuario.objects.get_or_create(usuario=request.user)

    if request.method == 'POST':
        pregunta_pk = request.POST.get('pregunta_pk')
        pregunta_respondida = QuizUser.intentos.select_related(
            'pregunta').get(pregunta__pk=pregunta_pk)
        respuesta_pk = request.POST.get('respuesta_pk')

        try:
            opcion_selecionada = pregunta_respondida.pregunta.opciones.get(
                pk=respuesta_pk)
        except ObjectDoesNotExist:
            raise Http404

        QuizUser.validate_intent(pregunta_respondida, opcion_selecionada)

        return redirect('resultado', pregunta_respondida.pk)

    else:
        pregunta = QuizUser.get_new_question()
        if pregunta is not None:
            QuizUser.create_intent(pregunta)

        context = {
            'pregunta': pregunta
        }

    return render(request, 'Play/play.html', context)


def resultado_pregunta(request, pregunta_respondida_pk):
    respondida = get_object_or_404(
        PreguntasRespondidas, pk=pregunta_respondida_pk)
    context = {
        'respondida': respondida
    }
    return render(request, 'Play/resultados.html', context)
