from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin , PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.http import HttpResponse
import json

from .models import Categoria, SubCategoria, Marca, UnidadMedida, Producto
from .forms import CategoriaForm, SubCategoriaForm, MarcaForm, UnidadMedidaForm, ProductoForm

#CATEGORIAS
class CategoriaView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    permission_required = "inv.view_categoria"
    model = Categoria
    template_name = "inv/categoria_list.html"
    context_object_name = "obj"
    login_url = "bases:login"

class CategoriaNew(SuccessMessageMixin, LoginRequiredMixin, generic.CreateView):
    model = Categoria
    template_name = "inv/categoria_form.html"
    context_object_name = "obj"
    form_class = CategoriaForm
    success_url = reverse_lazy("inv:categoria_list")
    login_url = "bases:login"
    success_message = "Categoría Creada Satisfactoriamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class CategoriaEdit(SuccessMessageMixin, LoginRequiredMixin, generic.UpdateView):
    model = Categoria
    template_name = "inv/categoria_form.html"
    context_object_name = "obj"
    form_class = CategoriaForm
    success_url = reverse_lazy("inv:categoria_list")
    login_url = "bases:login"
    success_message = "Categoría Actualizada Correctamente"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

# class CategoriaDel(LoginRequiredMixin, generic.DeleteView):
#     model = Categoria
#     template_name = "inv/catalogos_del.html"
#     context_object_name = "obj"
#     success_url = reverse_lazy("inv:categoria_list")
#     login_url = "bases:login"


#SUB CATEGORIAS
class SubCategoriaView(LoginRequiredMixin,PermissionRequiredMixin, generic.ListView):
    permission_required = "inv.view_subcategoria"
    model = SubCategoria
    template_name = "inv/subcategoria_list.html"
    context_object_name = "obj"
    login_url = "bases:login"

class SubCategoriaNew(LoginRequiredMixin, generic.CreateView):
    model = SubCategoria
    template_name = "inv/subcategoria_form.html"
    context_object_name = "obj"
    form_class = SubCategoriaForm
    success_url = reverse_lazy("inv:subcategoria_list")
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class SubCategoriaEdit(LoginRequiredMixin, generic.UpdateView):
    model = SubCategoria
    template_name = "inv/subcategoria_form.html"
    context_object_name = "obj"
    form_class = SubCategoriaForm
    success_url = reverse_lazy("inv:subcategoria_list")
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class SubCategoriaDel(LoginRequiredMixin, generic.DeleteView):
    model = SubCategoria
    template_name = "inv/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("inv:subcategoria_list")
    login_url = "bases:login"


#MARCAS
class MarcaView(LoginRequiredMixin, generic.ListView):
    model = Marca
    template_name = "inv/marca_list.html"
    context_object_name = "obj"
    login_url = "bases:login"

class MarcaNew(LoginRequiredMixin, generic.CreateView):
    model = Marca
    template_name = "inv/marca_form.html"
    context_object_name = "obj"
    form_class = MarcaForm
    success_url = reverse_lazy("inv:marca_list")
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class MarcaEdit(LoginRequiredMixin, generic.UpdateView):
    model = Marca
    template_name = "inv/marca_form.html"
    context_object_name = "obj"
    form_class = MarcaForm
    success_url = reverse_lazy("inv:marca_list")
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

#UNIDAD DE MEDIDA
class UnidadMedidaView(LoginRequiredMixin, generic.ListView):
    model = UnidadMedida
    template_name = "inv/unidadmedida_list.html"
    context_object_name = "obj"
    login_url = "bases:login"

class UnidadMedidaNew(LoginRequiredMixin, generic.CreateView):
    model = UnidadMedida
    template_name = "inv/unidadmedida_form.html"
    context_object_name = "obj"
    form_class = UnidadMedidaForm
    success_url = reverse_lazy("inv:unidadmedida_list")
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class UnidadMedidaEdit(LoginRequiredMixin, generic.UpdateView):
    model = UnidadMedida
    template_name = "inv/producto_form.html"
    context_object_name = "obj"
    form_class = UnidadMedidaForm
    success_url = reverse_lazy("inv:producto_list")
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

#PRODUCTO
class ProductoView(LoginRequiredMixin, generic.ListView):
    model = Producto
    template_name = "inv/producto_list.html"
    context_object_name = "obj"
    login_url = "bases:login"

class ProductoNew(LoginRequiredMixin, generic.CreateView):
    model = Producto
    template_name = "inv/producto_form.html"
    context_object_name = "obj"
    form_class = ProductoForm
    success_url = reverse_lazy("inv:producto_list")
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class ProductoEdit(LoginRequiredMixin, generic.UpdateView):
    model = Producto
    template_name = "inv/producto_form.html"
    context_object_name = "obj"
    form_class = ProductoForm
    success_url = reverse_lazy("inv:producto_list")
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

#BOTON DE DESACTIVAR
def categoria_inactivar(request, id):
    template_name = "inv/catalogos_del.html"
    contexto={}
    categoria = Categoria.objects.filter(pk=id).first()

    if not categoria:
        return HttpResponse('Categoría no existe ' + str(id))

    if request.method == 'GET':
        contexto = {'obj':categoria}
    
    if request.method == 'POST':
        if categoria.estado:
            categoria.estado = False
            categoria.save()
            contexto = {'obj':'OK'}
            
            return HttpResponse('Categoria Inactivada')
            
        else:
            categoria.estado = True
            categoria.save()
            contexto = {'obj':'OK'}
            return HttpResponse('Categoria Activada')
        
    return render(request, template_name,contexto)

def marca_inactivar(request, id):
    marca = Marca.objects.filter(pk=id).first()
    contexto = {}
    template_name = "inv/catalogos_del.html"

    if not marca:
        return HttpResponse("inv:marca_list")

    if request.method == 'GET':
        contexto = {'obj':marca}
    
    if request.method == 'POST':
        if marca.estado:
            marca.estado = False
            marca.save()
            contexto = {'obj':'OK'}
            return HttpResponse('Marca Inactivada')
        else:
            marca.estado = True
            marca.save()
            contexto = {'obj':'OK'}
            return HttpResponse('Marca Inactivada')

        

    return render(request, template_name,contexto)
    
def unidadmedida_inactivar(request, id):
    marca = UnidadMedida.objects.filter(pk=id).first()
    contexto = {}
    template_name = "inv/catalogos_del.html"

    if not marca:
        return redirect("inv:unidadmedida_list")

    if request.method == 'GET':
        contexto = {'obj':marca}
    
    if request.method == 'POST':
        if marca.estado:
            marca.estado = False
        else:
            marca.estado = True
        marca.save()
        return redirect("inv:unidadmedida_list")

    return render(request, template_name,contexto)

def producto_inactivar(request, id):
    prod = Producto.objects.filter(pk=id).first()
    contexto = {}
    template_name = "inv/catalogos_del.html"

    if not prod:
        return HttpResponse('Producto no existe ' + str(id))
    
    if request.method == 'GET':
        contexto = {'obj':prod}
    if request.method == 'POST':
        if prod.estado:
            prod.estado = False
            prod.save()
            contexto = {'obj':'OK'}
            return HttpResponse('Producto Inactivado')
        else:
            prod.estado = True
            prod.save()
            contexto = {'obj':'OK'}
            return HttpResponse('Producto Activado')
    return render(request, template_name,contexto)
