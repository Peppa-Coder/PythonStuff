from django.contrib import admin
from gestionPedidos.models import *

# Register your models here.

class ClientesAdmin(admin.ModelAdmin):
    list_display = ('nombre','direccion','telefono')
    search_fields = ('nombre',)

class ArticulosAdmin(admin.ModelAdmin):
    list_display = ('nombre','seccion','precio')
    search_fields = ('nombre',)
    list_filter = ('seccion',)

class PedidosAdmin(admin.ModelAdmin):
    list_filter = ('estado','fecha')
    date_hierarchy = 'fecha'

admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Pedidos, PedidosAdmin)