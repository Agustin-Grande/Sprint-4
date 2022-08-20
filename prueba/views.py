#Sprint 7 - Primera aplicacion

#Vamos a importar un método del módulo django.http llamado HttpResponse

from django.shortcuts import render, HttpResponse

from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.shortcuts import redirect

#Este método permite contestar a una petición devolviendo un código
#vamos a definir una vista para la portada y devolveremos HTML

#def home(request):
#    html_response = "<h1>Bienvenidos a mi sitio de prueba</h1>"
#    for i in range(10):
#        html_response += "<p>Línea " + str(i) + "</p>"
#
#    return HttpResponse(html_response)

def home(request):

    #Usaremos las sesiones para contar el numero de visitas al sitio
    #NUmero de visitas a esta view, como esta contado en la variable de sesion
    #Obtenemos el valor de la clave de sesion num_visits, estableciendo el valor a 0 si no habia
    #sido establecido anteriormente
    num_visits = request.session.get('num_visits',0)
    #Cada vez que se recibe la solicitud, incrementamos el valor y lo guardamos de vuelta en la sesion
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_visits':num_visits,
    }
    
       #utilizamos el método render del módulo http
    return render(request,"prueba/home.html", context=context)

#Cada vista se corresponde con una función del archivo views.py

#Se recibe un argumento llamado request, se trata de la petición

def about(request):
    html_response = "<h1>Quienes somos?</h1>"
    return HttpResponse(html_response)

@login_required
def contact(request):
    html_response = "<h1>Información de contacto</h1>"
    return HttpResponse(html_response)

#para ver los proyectos el usuario tiene que estar logueado
@login_required
def portfolio(request):
    html_response = "<h1>Proyectos/h1>"
    return HttpResponse(html_response)