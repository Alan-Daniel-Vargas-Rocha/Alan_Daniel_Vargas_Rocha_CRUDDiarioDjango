from django.forms import ModelForm
from .models import *

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile

        fields = ['nombre_completo', 'apellidos', 'fecha_nacimiento', 'email']


        labels = {
            'nombre_completo': 'Nombre completo del usuario',
            'apellidos': 'Apellidos',
            'fecha_nacimiento': 'Fecha de nacimiento',
            'email': 'Correo electrónico',
        }