from django.shortcuts import render
from .models import Genero,Alumno

# Create your views here.

def index(request):
    alumnos = Alumno.objects.all()
    context = {"alumnos":alumnos}
    return render(request,"alumnos/index.html",context)

def listadoSQL(request):

    Alumnos = Alumno.objects.raw("SELECT * FROM alumnos_alumno")
    context = {"alumnos":Alumnos}
    return render(request,"alumnos/listadoSQL.html",context)