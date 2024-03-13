from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path("", inicio, name="Inicio"),
    path("producto/", producto, name="Producto"),
    path("superadmin/", superadmin, name="Superadmin"),
    path("cliente/", cliente, name="Cliente"),
    path("entregables/", entregable, name="Entregables"),
    path("productoFormulario/", productoFormulario, name="Formularioproducto"),
    path("buscarProducto/", busquedaProducto, name="BuscarProducto"),
    path("resultados/", resultados, name="ResultadosBusqueda"),
]
