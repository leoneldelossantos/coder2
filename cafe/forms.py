from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from cafe.models import Cafe, Capsulas, Te, Avatar
from cafe.models import *

class CafeFormulario(forms.Form):
    tipo = forms.CharField(max_length=64)
    cantidad = forms.IntegerField(required=True, max_value=2000)
    descripcion = forms.CharField(required=False, max_length=1000)
    precio = forms.IntegerField(required=True, max_value=2000)
    
    
class CafeForm(forms.ModelForm):

    class Meta:
        model = Cafe
        fields = ['tipo', 'cantidad', 'descripcion', 'precio','fecha_entrega',]
        
class CapsulasFormulario(forms.Form):
    tipo = forms.CharField(max_length=64)
    cantidad = forms.IntegerField(required=True, max_value=2000)
    descripcion = forms.CharField(required=False, max_length=1000)
    precio = forms.IntegerField(required=True, max_value=2000)
    fecha_entrega = forms.IntegerField(required=True, max_value=2000)
    
class CapsulasForm(forms.ModelForm):

    class Meta:
        model = Capsulas
        fields = ['tipo', 'cantidad', 'descripcion', 'precio','fecha_entrega',]
           
class TeFormulario(forms.Form):
    tipo = forms.CharField(max_length=64)
    cantidad = forms.IntegerField(required=True, max_value=2000)
    descripcion = forms.CharField(required=False, max_length=1000)
    fecha_entrega = models.DateField(null=True)
    precio = forms.IntegerField(required=True, max_value=2000)
    
class TeForm(forms.ModelForm):

    class Meta:
        model = Te
        fields = ['tipo', 'cantidad', 'descripcion', 'fecha_entrega','precio',]
           
class UserRegisterForm(UserCreationForm):
    # Esto es un ModelForm
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'username', 'email', 'password1', 'password2']
 
class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'DNI', 'email',]

        
class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'email']
        
class AvatarFormulario(forms.ModelForm):

    class Meta:
        model = Avatar
        fields = ['imagen']
        
        

