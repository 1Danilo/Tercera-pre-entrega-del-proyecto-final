from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Producto
from AppCoder.forms import ProductoFormulario


def inicio(request):
    return render(request, "AppCoder/inicio.html")


def producto(request):
    return render(request, "AppCoder/producto.html")


def cliente(request):
    return render(request, "AppCoder/cliente.html")


def superadmin(request):
    return render(request, "AppCoder/superadmin.html")


def entregable(request):
    return render(request, "AppCoder/entregables.html")


def productoFormulario(request):

    if request.method == "POST":

        formulario1 = ProductoFormulario(request.POST)

        if formulario1.is_valid():
            info = formulario1.cleaned_data
            producto = Producto(nombre=info["nombre"], serie=info["serie"])
            producto.save()
            return render(request, "AppCoder/inicio.html")
    else:
        formulario1 = ProductoFormulario()

    return render(request, "AppCoder/productoFormulario.html", {"form1": formulario1})


def busquedaProducto(request):

    return render(request, "AppCoder/inicio.html")


def resultados(request):
    respuesta = ""

    if 'serie' in request.GET:
        serie = request.GET['serie']

        if serie:
            productos = Producto.objects.filter(serie__icontains=serie)
            return render(request, "Appcoder/inicio.html", {"productos": productos, "serie": serie})
        else:
            respuesta = "Por favor, ingrese un número de serie válido para buscar."
    else:
        respuesta = "No se enviaron datos."

    return render(request, "Appcoder/inicio.html", {"respuesta": respuesta})
