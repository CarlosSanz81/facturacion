from django.urls import path
from .views import ProveedorView, ProveedorNew, ProveedorEdit, proveedor_inactivar, \
                ComprasView, compras


urlpatterns = [
    path('proveedores/', ProveedorView.as_view(), name='proveedor_list'),
    path('proveedores/new/', ProveedorNew.as_view(), name='proveedor_new'),
    path('proveedores/edit/<int:pk>', ProveedorEdit.as_view(), name='proveedor_edit'),
    path('proveedores/inactivar/<int:id>', proveedor_inactivar, name='proveedor_inactivar'),

    path('compras/', ComprasView.as_view(), name="compras_list"),
    path('compras/new', compras, name = 'compras_new'),

]
