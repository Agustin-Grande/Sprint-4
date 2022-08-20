from django.apps import AppConfig


class PortfolioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portfolio'
    #Agregamos el campo verbose_name para mostrar un nombre mas descriptivo en el admin
    verbose_name = 'Portafolio'
