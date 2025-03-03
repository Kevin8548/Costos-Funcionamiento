from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def base(request):
    return render(request, "base.html", {})

def acerca(request):
    return render(request, "acercaProyecto.html", {})

def contacto(request):
    return render(request, "contacto.html", {})

def costos(request):
    return render(request, "costos.html", {})

def funcionamiento(request):
    return render(request, "funcionamiento.html", {})

def proyecto(request):
    return render(request, "proyecto.html", {})

def nosotros(request):
    return render(request, "sobreNosotros.html", {})
