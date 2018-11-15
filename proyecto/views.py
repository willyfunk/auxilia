from django.shortcuts import render
from django.http import HttpResponse
from .models import Persona
from django.shortcuts import redirect
#Importar usuario
from django.contrib.auth.models import User
#Sistema de autenticación
from django.contrib.auth import authenticate,logout, login as auth_login
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    usuario = request.session.get('usuario',None)
    return render(request,'index.html',{'name':'Registro de personas','usuario':usuario})


def formulario(request):
    usuario = request.session.get('usuario',None)
    return render(request, 'formulario.html',{'name':'Registro de personas','usuario':usuario})

def documentos(request):
    usuario = request.session.get('usuario',None)
    return render(request, 'documentos.html',{'name':'Registro de personas','usuario':usuario})

@login_required(login_url='login')
@staff_member_required(login_url='login')
def vistaFormulario(request):
    usuario = request.session.get('usuario',None)
    return render(request, 'vistaFormulario.html',{'persona': Persona.objects.all(),'name':'Registro de personas','usuario':usuario})

@login_required(login_url='login')
@staff_member_required(login_url='login')
def administrarMensajes(request,id):
    usuario = request.session.get('usuario',None)
    persona = Persona.objects.get(id=id)
    print(persona)
    return render(request,'administrarMensajes.html',{'persona':persona,'name':'Registro de personas','usuario':usuario})

def embajadas(request):
    usuario = request.session.get('usuario',None)
    return render(request, 'embajadas.html',{'name':'Registro de personas','usuario':usuario})    

def login(request):
    return render(request, 'login.html',{})

def login_iniciar(request):
    nombre_usuario = request.POST.get('nombre_usuario','')
    contrasenia = request.POST.get('contrasenia','')
    user = authenticate(username=nombre_usuario, password=contrasenia)
    if user is not None:
        auth_login(request, user)
        request.session['usuario'] = user.first_name+" "+user.last_name
        return redirect('index')
    else:
        return redirect('login')

@login_required(login_url='login')
@staff_member_required(login_url='login')
def cerrar_session(request):
    del request.session['usuario']
    logout(request)
    return redirect('index')

def crear(request):
    nombre = request.POST.get('nombre', '')
    apellido = request.POST.get('apellido', '')
    correo = request.POST.get('correo', '')
    telefono = request.POST.get('telefono', '')
    asunto = request.POST.get('asunto', '')
    mensaje = request.POST.get('mensaje', '')
    estado = request.POST.get('estado', '')
    respuesta = request.POST.get('respuesta','pendiente')
    persona = Persona(nombre=nombre, apellido=apellido, correo=correo,telefono=telefono, asunto=asunto,
                            mensaje=mensaje, estado=estado, respuesta=respuesta)
    persona.save()
    return redirect('formulario')

@login_required(login_url='login')
@staff_member_required(login_url='login')
def modificar(request,id):
    nombre = request.POST.get('nombre', '')
    apellido = request.POST.get('apellido', '')
    correo = request.POST.get('correo', '')
    telefono = request.POST.get('telefono', '')
    asunto = request.POST.get('asunto', '')
    mensaje = request.POST.get('mensaje', '')
    estado = request.POST.get('estado', '')
    respuesta = request.POST.get('respuesta', '')
    persona = Persona.objects.get(pk=id)
    persona.nombre = nombre
    persona.apellido = apellido
    persona.correo  = correo 
    persona.telefono = telefono
    persona.asunto = asunto 
    persona.mensaje = mensaje
    persona.estado = estado
    persona.respuesta = respuesta
    persona.save()
    return redirect('index')