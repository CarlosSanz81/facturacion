from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required, permission_required

from django.http import HttpResponse
#import json
from bases.views import SinPrivilegios
from .models import Proveedor
from cmp.forms import ProveedorForm


class ProveedorView(SinPrivilegios, generic.ListView):
    permission_required = "cmp.view_proveedor"
    model = Proveedor
    template_name = "cmp/proveedor_list.html"
    context_object_name = "obj"
    

class ProveedorNew(SuccessMessageMixin, SinPrivilegios, generic.CreateView):
    model = Proveedor
    template_name = "cmp/proveedor_form.html"
    context_object_name = "obj"
    form_class = ProveedorForm
    success_url = reverse_lazy("cmp:proveedor_list")
    success_message = "Proveedor Creado"
    permission_required ="cmp.add_proveedor"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        print(self.request.user.id)
        return super().form_valid(form)

class ProveedorEdit(SuccessMessageMixin, SinPrivilegios, generic.UpdateView):
    model = Proveedor
    template_name = "cmp/proveedor_form.html"
    context_object_name = "obj"
    form_class = ProveedorForm
    success_url = reverse_lazy("cmp:proveedor_list")
    success_message = "Proveedor Actualizado Correctamente"
    permission_required ="cmp.change_proveedor"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        # print(self.request.user.id)
        return super().form_valid(form)


#DESACTIVACIONES
@login_required(login_url = '/login/')
@permission_required('cmp.change_proveedor', login_url= 'bases:sin_privilegios')
def proveedor_inactivar(request, id):
    template_name='cmp/inactivar_prv.html'
    contexto={}
    prv = Proveedor.objects.filter(pk=id).first()

    if not prv:
        return HttpResponse('Proveedor no existe ' + str(id))
    
    if request.method == 'GET':
        contexto={'obj':prv}
             
    if request.method == 'POST':
        if prv.estado:
            prv.estado = False
            prv.save()
            contexto = {'obj':'OK'}
            return HttpResponse('Proveedor Inactivado')
        else:
            prv.estado = True
            prv.save()
            contexto = {'obj':'OK'}
            return HttpResponse('Proveedor Activado')

    return render(request, template_name,contexto)