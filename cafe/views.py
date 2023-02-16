
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from cafe.models import Cafe, Capsulas, Te, Cliente
from cafe.forms import UserRegisterForm, UserUpdateForm, AvatarFormulario

from cafe.views import *


@login_required 
def inicio(request):
    return render(
        request=request,
        template_name='cafe/inicio.html',
    )



class CafeListView(LoginRequiredMixin,ListView):
    model = Cafe
    template_name = "cafe/lista_cafe.html"


class CafeCreateView(CreateView):
    model = Cafe
    fields = ['tipo', 'cantidad', 'descripcion', 'precio', 'fecha_entrega']
    success_url = reverse_lazy('crear_cafe')
    template_name = "cafe/formulario_cafe.html"


class CafeDetailView(LoginRequiredMixin, DetailView):
    model = Cafe
    success_url = reverse_lazy('listar_cafe')
    template_name = "cafe/detalle_cafe.html"


class CafeUpdateView(LoginRequiredMixin, UpdateView):
    model = Cafe
    fields =  ['tipo', 'cantidad', 'descripcion', 'precio', 'fecha_entrega']
    success_url = reverse_lazy('listar_cafe')
    template_name = "cafe/formulario_cafe.html"


class CafeDeleteView(LoginRequiredMixin, DeleteView):
    model = Cafe
    success_url = reverse_lazy('listar_cafe')
    template_name = "cafe/confirmar_eliminacion_cafe.html"
     

class CapsulasListView(LoginRequiredMixin, ListView):
    model = Capsulas
    template_name = "cafe/lista_capsulas.html"


class CapsulasCreateView(LoginRequiredMixin, CreateView):
    model = Capsulas
    fields = ['tipo', 'cantidad', 'descripcion', 'precio', 'fecha_entrega']
    success_url = reverse_lazy('listar_capsulas')
    template_name = "cafe/formulario_capsulas.html"


class CapsulasDetailView(LoginRequiredMixin, DetailView):
    model = Capsulas
    success_url = reverse_lazy('listar_capsulas')
    template_name = "cafe/detalle_capsulas.html"


class CapsulasUpdateView(LoginRequiredMixin, UpdateView):
    model = Capsulas
    fields =  ['tipo', 'cantidad', 'descripcion', 'precio', 'fecha_entrega']
    success_url = reverse_lazy('listar_capsulas')
    template_name = "cafe/formulario_capsulas.html"


class CapsulasDeleteView(LoginRequiredMixin, DeleteView):
    model = Capsulas
    success_url = reverse_lazy('listar_Capsulas')
    template_name = "cafe/confirmar_eliminacion_capsulas.html"
    

class TeListView(LoginRequiredMixin, ListView):
    model = Te
    template_name = "cafe/lista_te.html"


class TeCreateView(LoginRequiredMixin, CreateView):
    model = Te
    fields = ['tipo', 'cantidad', 'descripcion', 'precio', 'fecha_entrega']
    success_url = reverse_lazy('listar_Te')
    template_name = "cafe/formulario_te.html"


class TeDetailView(LoginRequiredMixin, DetailView):
    model = Te
    success_url = reverse_lazy('listar_Te')
    template_name = "cafe/detalle_Te.html"


class TeUpdateView(LoginRequiredMixin, UpdateView):
    model = Te
    fields =  ['tipo', 'cantidad', 'descripcion', 'precio', 'fecha_entrega']
    success_url = reverse_lazy('listar_Te')
    template_name = "cafe/formulario_te.html"


class TeDeleteView(LoginRequiredMixin, DeleteView):
    model = Te
    success_url = reverse_lazy('listar_Te')
    template_name = "cafe/confirmar_eliminacion_te.html"     

class ClienteListView(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = "cafe/lista_cliente.html"


class ClienteCreateView(LoginRequiredMixin, CreateView):
    model = Cliente
    fields = ['nombre', 'apellido', 'DNI', 'email']
    success_url = reverse_lazy('listar_cliente')
    template_name = "cafe/formulario_cliente.html"


class ClienteDetailView(LoginRequiredMixin, DetailView):
    model = Cliente
    success_url = reverse_lazy('listar_cliente')
    template_name = "cafe/detalle_cliente.html"


class ClienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Cliente
    fields = ['nombre', 'apellido', 'DNI', 'email']
    success_url = reverse_lazy('listar_cliente')
    template_name = "cafe/formulario_cliente.html"

    
def registro(request):
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():
            formulario.save()  
            url_exitosa = reverse('inicio')
            return redirect(url_exitosa)
    else:  # GET
        formulario = UserRegisterForm()
    return render(
        request=request,
        template_name='cafe/registro.html',
        context={'form': formulario},
    )


def login_view(request):
    next_url = request.GET.get('next')
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data
            usuario = data.get('username')
            password = data.get('password')
            user = authenticate(username=usuario, password=password)
            if user:
                login(request=request, user=user)
                if next_url:
                    return redirect(next_url)
                url_exitosa = reverse('inicio')
                return redirect(url_exitosa)
    else:  
        form = AuthenticationForm()
    return render(
        request=request,
        template_name='cafe/login.html',
        context={'form': form},
    )
    
class CustomLogoutView(LogoutView):
    template_name = 'cafe/logout.html'


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('inicio')
    template_name = 'cafe/formulario_perfil.html'

    def get_object(self, queryset=None):
        return self.request.user
    

def agregar_avatar(request):
    if request.method == "POST":
        formulario = AvatarFormulario(request.POST, request.FILES) 

        if formulario.is_valid():
            avatar = formulario.save()
            avatar.user = request.user
            avatar.save()
            url_exitosa = reverse('inicio')
            return redirect(url_exitosa)
    else:  
        formulario = AvatarFormulario()
    return render(
        request=request,
        template_name='cafe/formulario_avatar.html',
        context={'form': formulario},
    )
    

def acerca(request):
    return render(
        request=request,
        template_name='cafe/acerca.html',
    )

