from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Proveedor
from cmp.forms import ProveedorForm


class ProveedorView(LoginRequiredMixin, generic.ListView):
    model = Proveedor
    template_name = "cmp/proveedor_list.html"
    context_object_name = "obj"
    login_url = "bases:login"

class ProveedorNew(LoginRequiredMixin, generic.CreateView):
    model = Proveedor
    template_name = "cmp/proveedor_form.html"
    context_object_name = "obj"
    form_class = ProveedorForm
    success_url = reverse_lazy("cmp:proveedor_list")
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        print(self.request.user.id)
        return super().form_valid(form)

class ProveedorEdit(LoginRequiredMixin, generic.UpdateView):
    model = Proveedor
    template_name = "cmp/proveedor_form.html"
    context_object_name = "obj"
    form_class = ProveedorForm
    success_url = reverse_lazy("cmp:proveedor_list")
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        # print(self.request.user.id)
        return super().form_valid(form)


#DESACTIVACIONES
def proveedor_inactivar(request, id):
    prov = Proveedor.objects.filter(pk=id).first()
    contexto = {}
    template_name = "./inv/catalogos_del.html"

    if not prov:
        return redirect("cmp:proveedor_list")

    if request.method == 'GET':
        contexto = {'obj':prov}
            
    if request.method == 'POST':
        if prov.estado:
            prov.estado = False
        else:
            prov.estado = True
        prov.save()
        return redirect("cmp:proveedor_list")

    return render(request, template_name,contexto)