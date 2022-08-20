from django.urls import path
from . import views

#Creamos la direcion de la app contact
urlpatterns = [
    path('', views.contact, name="contact"),

]