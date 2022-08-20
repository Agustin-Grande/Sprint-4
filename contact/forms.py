#Importamos forms
from django import forms

#creamos la calse ContactForm que hereda de la clase padre Forms
#Demeos indicar los campos y su tipo

class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", required=True)
    email = forms.EmailField(label="Email", required=True)
    content = forms.CharField(label="Contenido", required=True, widget=forms.Textarea())