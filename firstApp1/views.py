from django.shortcuts import render

# Create your views here.
def index(request):
    data = {
        "Nombre" : 'Yesenia',
        "Apellido" : 'Concha Chamorro',
        "Profesion" : 'Estudiante de Ingeniería en Informática',
        "Edad" : '24 años',
        "Ciudad" : 'Constitución',
        "Proyectos": 'Bailes de Danza, Flamenco y Tango',
        "Imagen" : '/static/img/perfil.jpg',

    }
    return render (request, 'index.html', data)

def proyecto1(request):
    data = {
        "NombreProyecto" : 'FLAMENCO',
        "Detalle" : 'Este proyecto tiene por objetivo poder incentivar a las personas a poder bailar de una forma más sofisticada el flamenco',
        "Cliente" : 'Dirigido a todo público en general',
        "Año" : '2008',
        "Lugar" : 'Cada jueves en la cede central. Talca',
        "Nivel" : 'Básico, internedio y avanzado',
        "Planes" : 'Planes y precios para todo tipo de bolsillo',
        "Mas" : 'Aprende con nosotros, será una buena experiencia ',
        "Imagen" : '/static/img/proyecto1.jpg'
    
    }
    return render (request, 'proyectos.html', data)

def proyecto2(request):
    data = {
        "NombreProyecto" : 'TANGO',
        "Detalle" : 'Incentivar a todo público en general a bailar Tango',
        "Cliente" : 'Dirigido a todo público en general',
        "Año" : '2005',
        "Lugar" : 'Cada Lunes en la plaza central. Talca',
        "Nivel" : 'Básico, internedio y avanzado',
        "Planes" : 'Planes y precios para todo tipo de bolsillo',
        "Mas" : 'Aprende con nosotros, será una buena experiencia ',        
        "Imagen" : '/static/img/proyecto2.jpg'
    
    }
    return render (request, 'proyectos.html', data)

def proyecto3(request):
    data = {
        "NombreProyecto" : 'DANZA',
        "Detalle" : 'Atrevete y aprende danza',
        "Cliente" : 'Dirigido a todo público en general',
        "Año" : '2009',
        "Lugar" : 'Cada Martes en la muelle. Constitución',
        "Nivel" : 'Básico, internedio y avanzado',
        "Planes" : 'Planes y precios para todo tipo de bolsillo',
        "Mas" : 'Aprende con nosotros, será una buena experiencia ', 
        "Imagen" : '/static/img/proyecto3.jpg'
    
    }
    return render (request, 'proyectos.html', data)