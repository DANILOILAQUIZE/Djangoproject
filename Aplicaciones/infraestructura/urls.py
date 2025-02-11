from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    
    
    path('escuela/agregarEscuela/', views.agregarEscuela, name='agregarEscuela'),
    path('escuela/guardarEscuela/', views.guardarEscuela, name='guardarEscuela'),
    path('escuela/listarEscuelas/', views.listarEscuelas, name='listarEscuelas'),
    path('editarEscuela/<int:id>/', views.editarEscuela, name='editarEscuela'),
    path('actualizarEscuela/<int:id>/', views.actualizarEscuela, name='actualizarEscuela'),
    path('eliminarEscuela/<int:id>/', views.eliminarEscuela, name='eliminarEscuela'),
    
    path('proveedor/agregarProveedor/', views.agregarProveedor, name='agregarProveedor'),
    path('proveedor/guardarProveedor/', views.guardarProveedor, name='guardarProveedor'),
    path('proveedor/listarProveedores/', views.listarProveedores, name='listarProveedores'),
    path('editarProveedor/<int:id>/', views.editarProveedor, name='editarProveedor'),
    path('actualizarProveedor/<int:id>/', views.actualizarProveedor, name='actualizarProveedor'),
    path('eliminarProveedor/<int:id>/', views.eliminarProveedor, name='eliminarProveedor'),
    
    path('proyecto/agregarProyecto/', views.agregarProyecto, name='agregarProyecto'),
    path('proyecto/guardarProyecto/', views.guardarProyecto, name='guardarProyecto'),
    path('proyecto/listarProyectos/', views.listarProyectos, name='listarProyectos'),
    path('editarProyecto/<int:id>/', views.editarProyecto, name='editarProyecto'),
    path('actualizarProyecto/<int:id>/', views.actualizarProyecto, name='actualizarProyecto'),
    path('eliminarProyecto/<int:id>/', views.eliminarProyecto, name='eliminarProyecto'),
    
    path('plazo/agregarPlazo/', views.agregarPlazo, name='agregarPlazo'),
    path('plazo/guardarPlazo/', views.guardarPlazo, name='guardarPlazo'),   
    path('plazo/listarPlazos/', views.listarPlazos, name='listarPlazos'),
    path('editarPlazo/<int:id>/', views.editarPlazo, name='editarPlazo'),
    path('actualizarPlazo/<int:id>/', views.actualizarPlazo, name='actualizarPlazo'),
    path('eliminarPlazo/<int:id>/', views.eliminarPlazo, name='eliminarPlazo'),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
