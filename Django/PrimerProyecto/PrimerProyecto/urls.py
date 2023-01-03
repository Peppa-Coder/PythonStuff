"""PrimerProyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from PrimerProyecto.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', saludo),
    path('fechaHora/', fecha),
    # Para indicarle django que en la vista que se trabajará con parametros en la url, se utiliza <parametro>
    # Todo lo que hay en una url es de tipo texto, por lo tanto, en este caso como es una año, debe transformarse a entero
    path('calculaEdad/<int:edad>/<int:anio>', calcula_edad),
    path('pruebaPlantilla/', prueba_plantilla),
    path('pruebaHerencia/', prueba_herencia),
]
