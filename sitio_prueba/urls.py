"""sitio_prueba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
#importamos tambien include para decirle que vaya a buscar el archivo de urls de la aplicacion contact
from django.urls import path,include

#Del package prueba (fijarse que tiene __init.py__) importamos el módulo views
#es decir, de la app prueba importamos las vistas. 

from prueba import views

#agregamos la clase settings para poder verificar si se usa el modo debug

from django.conf    import settings

#agregamos las dos vistas que venimos trabajando
from prueba import views as prueba_views
from portfolio import views as portfolio_views



urlpatterns = [
    #Creamos un patrón url, en la raíz del sitio (cadena vacía) desde el que llamaremos a la vista views.home que tiene el nombre home.
    path('',prueba_views.home, name="home"), 
    path('about/',prueba_views.about, name="about"), 
    path('portfolio/',portfolio_views.portfolio, name="portfolio"), #en este indicamos que utilice la vista porfolio
    path('admin/', admin.site.urls),
    #agregamos un path de paginas
    path('contact/', include('contact.urls')),
    #Agregamos las direcciones de autenticacion (login, logout, gestion password)
    path('accounts/',include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)