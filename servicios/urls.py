from django.urls import path
from . import views # Se pune un punto porque el views viene de la misma carpeta
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.servicios, name="Servicios"),
]

