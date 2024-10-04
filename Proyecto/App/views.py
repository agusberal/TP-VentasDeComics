from django.shortcuts import render,get_object_or_404,redirect
from .forms import * 
from .models import *
#importamos la libreria de logout
from django.contrib.auth import logout
#-->importamos la libreria de permisos
from django.contrib.auth.decorators import login_required,permission_required


# Create your views here.
def Home(request):
    buscar=Comics.objects.all().order_by('-Codigo')[:3]
    data={
        'forms':buscar
    }
    return render (request,'index.html',data)

def Agregar(request):
    data={
        'forms':NuevoComics()
    }  
    if request.method=='POST':
        query = NuevoComics(data=request.POST,files=request.FILES)
        if query.is_valid():
            query.save()
            data['mensaje']= "Datos Registrados"
        else:
            data['forms']=NuevoComics
    return render (request,'Pages/agregar.html', data)

def verProductos(request):
    #--->Traemos todos los elementos de la tabla
    buscar=Comics.objects.all()
    data={
        'forms':buscar
    }
    return render(request, 'Pages/visualizar.html',data)