from django.shortcuts import render

#importamos el modelo Project a la vista
from .models import Project

# Create your views here.


# recuperar los registros de la tabla Projects que maneja nuestro modelo ORM 
# a través una lista de objetos interna y un método .all() que hace referencia a todos sus objetos:
def portfolio(request):
    projects = Project.objects.all() 
    return render(request, "portfolio/portfolio.html", {'projects':projects})

#tenemos que inyectar estos proyectos en el template. 
# Para hacerlo simplemente enviamos a la función render un tercer parámetro con un diccionario
# y los valores que queremos inyectar.