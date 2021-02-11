from django.shortcuts import render
from servicios.models import Servicio # traer desde models.py de al App Servicio

# Create your views here.
def servicios(request):
    # aqui se deben importar todos los servicios cargados desde el Panel de Administración
    # y decile que los muestre en el template
    servicios=Servicio.objects.all() # importe todos los objetos que hayamos construido
    return render(request,"servicios/servicios.html",{"servicios": servicios}) #return HttpResponse("Servicios")

