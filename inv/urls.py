from django.urls import path

from .views import CategoriaView, CategoriaNew, CategoriaEdit, categoria_inactivar, \
    SubCategoriaView, SubCategoriaNew, SubCategoriaEdit, SubCategoriaDel, \
    MarcaView, MarcaNew, MarcaEdit, marca_inactivar, \
    UnidadMedidaView, UnidadMedidaNew, UnidadMedidaEdit, unidadmedida_inactivar, \
    ProductoView, ProductoNew, ProductoEdit, producto_inactivar


urlpatterns = [
    path('categorias/', CategoriaView.as_view(), name='categoria_list'),
    path('categorias/new', CategoriaNew.as_view(), name='categoria_new'),
    path('categorias/edit/<int:pk>/', CategoriaEdit.as_view(), name='categoria_edit'),
    path('categorias/inactivar/<int:id>/', categoria_inactivar, name='categoria_inactivar'),
    
    path('subcategorias/', SubCategoriaView.as_view(), name='subcategoria_list'),
    path('subcategorias/new', SubCategoriaNew.as_view(), name='subcategoria_new'),
    path('subcategorias/edit/<int:pk>/', SubCategoriaEdit.as_view(), name='subcategoria_edit'),
    path('subcategorias/delete/<int:pk>/', SubCategoriaDel.as_view(), name='subcategoria_del'),

    path('marca/', MarcaView.as_view(), name='marca_list'),
    path('marca/new', MarcaNew.as_view(), name='marca_new'),
    path('marca/edit/<int:pk>/', MarcaEdit.as_view(), name='marca_edit'),
    path('marca/inactivar/<int:id>/', marca_inactivar, name='marca_inactivar'),

    path('unidadmedida/', UnidadMedidaView.as_view(), name='unidadmedida_list'),
    path('unidadmedida/new', UnidadMedidaNew.as_view(), name='unidadmedida_new'),
    path('unidadmedida/edit/<int:pk>/', UnidadMedidaEdit.as_view(), name='unidadmedida_edit'),
    path('unidadmedida/inactivar/<int:id>/', unidadmedida_inactivar, name='unidadmedida_inactivar'),

    path('producto/', ProductoView.as_view(), name='producto_list'),
    path('producto/new', ProductoNew.as_view(), name='producto_new'),
    path('producto/edit/<int:pk>/', ProductoEdit.as_view(), name='producto_edit'),
    path('producto/inactivar/<int:id>/', producto_inactivar, name='producto_inactivar'),
]
