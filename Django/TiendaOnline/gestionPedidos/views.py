from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos

# Create your views here.
def busqueda_productos(request):
    return render(request, 'busqueda_productos.html')


def buscar(request):
    if request.GET["prd"]:
        #mensaje = 'Artículo buscado: %r' % request.GET["prd"]
        #El método get devuelve un objeto
        producto = request.GET["prd"]
        if len(producto) > 20:
            mensaje = 'Texto de búsqueda demasiado largo'
        else:
            #Usamos el método filter para filtrar los objetos que contengan el nombre del producto que se ha introducido en el formulario 
            #nombre_icontains sirve como un LIKE en una consulta SQL, el cual busca un patron especificado
            articulos = Articulos.objects.filter(nombre__icontains=producto)
            num_resultados = len(Articulos.objects.filter(nombre__icontains=producto))
            diccionario = {'articulos': articulos, 'query': producto, 'num_resultados': num_resultados}
            return render (request, template_name='resultados_busqueda.html', context=diccionario)
    else:
        mensaje = 'No has introducido ningún producto'
    return HttpResponse(mensaje)

def contacto(request):
    if request.method == "POST":
        if request.POST["asunto"] == "" or request.POST["email"] == "" or request.POST["mensaje"] == "":
            return render(request, 'campos_obligatorios.html', {'error':'Todos los campos son obligatorios'})
        else:
            asunto = request.POST["asunto"]
            email = request.POST["email"]
            mensaje = request.POST["mensaje"]
            diccionario = {'asunto':asunto, 'email':email, 'mensaje':mensaje}
            return render(request, 'gracias.html', context=diccionario)
    return render(request, 'contacto.html')