from django.shortcuts import render, HttpResponse

# Create your views here.
# Crear tantas views como URLs tenga el proyecto

def home(request):
    return render(request,"ProyectoWebApp/home.html") #HttpResponse("Home")

def tienda(request):
    return render(request,"ProyectoWebApp/tienda.html") #return HttpResponse("Tienda")


def contacto(request):
    return render(request,"ProyectoWebApp/contacto.html") #return HttpResponse("Contacto")
    