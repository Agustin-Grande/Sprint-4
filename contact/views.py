from django.shortcuts import render, redirect
from django.urls import reverse
#importamos el modulo donde esta la clase ContactForm
from .forms import ContactForm

from .models import Contact, Participant, Project

from datetime import date, timedelta

from django.db.models import F


# Create your views here.


#Agregamos la vista de contacto que teniamos en la aplicacion de prueba
def contact(request):
    #creamos una isntancia del formulario
    contact_form = ContactForm
    #validamos que ocurrio una peticion POST
    if request.method == "POST":
        #Traemos los datos enviados
        contact_form = contact_form(data=request.POST)
        #Chequeamos que los datos son validos, de ser asi, los asignamos a una variable
        if contact_form.is_valid():
            nameReceived = request.POST.get('name','')
            emailReceived = request.POST.get('email','')
            contentReceived = request.POST.get('content','')
            #obtenemos un proyecto, en este caso el de id 1, en este caso podriamos
            #modificar el fomulario para que consulte sobre que proyecto hacemos el contacto
            projectReceived= Project.objects.get(pk=1)
           
            #guardamos la informacion recibida en al base de datos
            contacto = Contact(name=nameReceived,email=emailReceived,content=contentReceived,pub_date=date.today(), project=projectReceived)
            contacto.save()

            #creamos un listado de participantes referentes del contacto, nuevamente como en el caso anterior
            #le podriamos haber pedido que lo ingrese por el formulario, por simplicidad los creamos aca
            participante1 = Participant.objects.create(name='Jose',email='jose@gmail.com')
            contacto.participants.add(participante1)

            #agregamos mas participantes
            #participante2 = Participant.objects.create(name='Pedro',email='pedro@gmail.com')
            #participante3 = Participant.objects.create(name='Julieta',email='julieta@gmail.com')
            #participante4 = Participant.objects.create(name='Yamila',email='yamila@gmail.com')
            #contacto.participants.add(participante2,participante3,participante4)

          

            #1-todos los contactos
            #all_contacts = Contact.objects.all()

            #2-agregando un filtro para los del año 2020
            filter_contacts = Contact.objects.filter(pub_date__year=2020)

            #3-encadenando filtros, los contactos que tengan de nombre Santigao, sacando los que se crearon hoy y filtrando los que sean de 2020
            #filter_contacts = Contact.objects.filter(name='Santiago').exclude(pub_date__gte=date.today()).filter(pub_date__year=2020)

            #4-Unicidad de query sets
            #q1=Contact.objects.filter(name='Santiago')
            #q2= q1.exclude(pub_date__gte=date.today())
            #q3= q1.filter(pub_date__gte=date.today())

            #filter_contacts = q3

            #5-Limite de los query sets, traigo solo 3 contactos
            #filter_contacts = Contact.objects.all()[:3]

            #6-Ordenar el resultado del filtro por nombre
            #filter_contacts = Contact.objects.all().order_by('name')

            #7-Campos de busqueda
            #filter_contacts = Contact.objects.filter(name__exact='Santiago')
            #filter_contacts = Contact.objects.filter(name__iexact='santiago')
            #filter_contacts = Contact.objects.filter(name__contains='tiago')
            #filter_contacts = Contact.objects.filter(pub_date__gte=date.today())
            #filter_contacts = Contact.objects.filter(pub_date__lte=date.today())

            #8-Busquedas de relaciones
            #filter_contacts = Contact.objects.filter(project__title__contains='banking')

            #9-busqueda con campos del modelo
            #filter_contacts = Contact.objects.filter(participants__name=F('name'))
            #filter_contacts = Contact.objects.filter(mod_date__gt=F('pub_date') + timedelta(days=3))

            #10 Borrado de objetos
            #Contact.objects.filter(name='Silvina').delete()

            #11 Actualzacion de objetos
            #Contact.objects.filter(pub_date__year=2020).update(mod_date=date.today())
            #filter_contacts = Contact.objects.filter(pub_date__year=2020)

            #12 Navegando las relaciones muchos a muchos
            #c = Contact.objects.get(id=3)
            #c.participants.all() # devuelve todos los participantes para este contacto.
            #c.participants.count()
            #c.participants.filter(name__contains='Jose')

            #p = Participant.objects.get(id=1)
            #p.entry_set.all() # Deveuelve todos los contactos para este participante

            #filter_contacts = c 

            #return render(request, "contact/contact_list.html", {'contacts':all_contacts})
            return render(request, "contact/contact_list.html", {'contacts':filter_contacts})

    #En lugar de renderizar el template de contacto hacemos un redireccionamiento enviando una variable OK        
    return render(request,'contact/contact.html',{'form': contact_form})