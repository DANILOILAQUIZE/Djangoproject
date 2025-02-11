from django.shortcuts import render, redirect
from .models import Escuela, Proveedor, ProyectoConstruccion, Plazo     
from django.contrib import messages
from decimal import Decimal
# Create your views here.

def index(request):
    return render(request, 'index.html')

def agregarEscuela(request):
    return render(request, 'escuela/agregarEscuela.html')
def guardarEscuela(request):
    nombre = request.POST['nombre']
    direccion = request.POST['direccion']
    telefono = request.POST.get('telefono', '')  # Opcional
    correo = request.POST.get('correo', '')  # Opcional
    imagen = request.FILES.get('imagen', None)  # Imagen opcional

        # Guardar en la base de datos
    Escuela.objects.create(
        nombre=nombre,
        direccion=direccion,
        telefono=telefono,
        correo=correo,
        imagen=imagen
    )

    messages.success(request, '¡Escuela guardada exitosamente!')
    return redirect('agregarEscuela')  # Redirige a la vista de agregar escuela

def listarEscuelas(request):
    escuelas = Escuela.objects.all()
    return render(request, 'escuela/listarEscuela.html', {'escuelas': escuelas})

def editarEscuela(request, id):
    escuela = Escuela.objects.get(id=id)
    return render(request, 'escuela/editarEscuela.html', {'escuela': escuela})
def actualizarEscuela(request, id):
    escuela = Escuela.objects.get(id=id)
    escuela.nombre = request.POST['nombre']
    escuela.direccion = request.POST['direccion']
    escuela.telefono = request.POST['telefono'] 
    escuela.correo = request.POST['correo']
    escuela.imagen = request.FILES.get('imagen', escuela.imagen)  # Imagen opcional

    escuela.save()
    messages.success(request, '¡Escuela Editada exitosamente!')

    return redirect('listarEscuelas')

def eliminarEscuela(request, id):
    escuela = Escuela.objects.get(id=id)
    escuela.delete()
    messages.success(request, '¡Escuela Eliminada exitosamente!')

    return redirect('listarEscuelas')

#=======================================================================================================
#PROVEEDOR

def agregarProveedor(request):
    return render(request, 'proveedor/agregarProveedor.html')


def guardarProveedor(request):
    nombre = request.POST['nombre']
    contacto = request.POST['contacto']  
    telefono = request.POST['telefono']  
    correo = request.POST['correo'] 
    direccion = request.POST['direccion']


    Proveedor.objects.create(
        nombre=nombre,
        contacto=contacto,
        telefono=telefono,
        correo=correo,
        direccion=direccion
    )

    messages.success(request, '¡Proveedor guardado exitosamente!')
    return redirect('agregarProveedor')  # Redirige a la vista de agregar proveedor

def listarProveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedor/listarProveedor.html', {'proveedores': proveedores})

def editarProveedor(request, id):
    proveedor = Proveedor.objects.get(id=id)
    return render(request, 'proveedor/editarProveedor.html', {'proveedor': proveedor})

def actualizarProveedor(request, id):
    proveedor = Proveedor.objects.get(id=id)
    proveedor.nombre = request.POST['nombre']
    proveedor.contacto = request.POST['contacto']  
    proveedor.telefono = request.POST['telefono']  
    proveedor.correo = request.POST['correo'] 
    proveedor.direccion = request.POST['direccion']

    proveedor.save()
    messages.success(request, '¡Proveedor editado exitosamente!')
    return redirect('listarProveedores')

def eliminarProveedor(request, id):
    proveedor = Proveedor.objects.get(id=id)
    proveedor.delete()
    messages.success(request, '¡Proveedor eliminado exitosamente!')
    return redirect('listarProveedores')


#=======================================================================================================
#PROVEEDOR

def agregarProyecto(request):
    escuelas = Escuela.objects.all()
    proveedores = Proveedor.objects.all()
    return render(request, 'proyecto/agregarProyecto.html', {'escuelas': escuelas, 'proveedores': proveedores})

def guardarProyecto(request):
    escuela_id = request.POST['escuela']
    proveedor_id = request.POST['proveedor']
    nombre = request.POST['nombre']
    descripcion = request.POST['descripcion']
    fecha_inicio = request.POST['fecha_inicio']
    fecha_fin = request.POST['fecha_fin']
    presupuesto = request.POST['presupuesto']

    ProyectoConstruccion.objects.create(
        escuela_id=escuela_id,
        proveedor_id=proveedor_id,
        nombre=nombre,
        descripcion=descripcion,
        fecha_inicio=fecha_inicio,
        fecha_fin=fecha_fin,
        presupuesto=presupuesto
    )
    messages.success(request, 'Proyecto guardado exitosamente!')
    return redirect('agregarProyecto')

def listarProyectos(request):
    proyectos = ProyectoConstruccion.objects.all()
    return render(request, 'proyecto/listarProyecto.html', {'proyectos': proyectos})

def editarProyecto(request, id):
    proyecto = ProyectoConstruccion.objects.get(id=id)
    escuelas = Escuela.objects.all()
    proveedores = Proveedor.objects.all()
    return render(request, 'proyecto/editarProyecto.html', {'proyecto': proyecto, 'escuelas': escuelas, 'proveedores': proveedores})


def actualizarProyecto(request, id):
    proyecto = ProyectoConstruccion.objects.get(id=id)
    proyecto.escuela_id = request.POST['escuela']
    proyecto.proveedor_id = request.POST['proveedor']
    proyecto.nombre = request.POST['nombre']
    proyecto.descripcion = request.POST['descripcion']
    proyecto.fecha_inicio = request.POST['fecha_inicio']
    proyecto.fecha_fin = request.POST['fecha_fin']
    precio= request.POST['presupuesto'].replace(',', '')  # Elimina las comas
    proyecto.presupuesto = Decimal(precio)

    proyecto.save()
    messages.success(request, 'Proyecto editado exitosamente!')
    return redirect('listarProyectos')

def eliminarProyecto(request, id):
    proyecto = ProyectoConstruccion.objects.get(id=id)
    proyecto.delete()
    messages.success(request, 'Proyecto eliminado exitosamente!')
    return redirect('listarProyectos')

#=======================================================================================
#PLAZOS

def agregarPlazo(request):
    proyectos = ProyectoConstruccion.objects.all()
    return render(request, 'plazo/agregarPlazo.html', {'proyectos': proyectos})

def guardarPlazo(request):
    if request.method == "POST":
        proyecto_id = request.POST['proyecto']
        descripcion = request.POST['descripcion']
        fecha_limite = request.POST['fecha_limite']
        completado = request.POST.get('completado') == 'on'  # Convierte "on" en True, si no está presente será False

        Plazo.objects.create(
            proyecto_id=proyecto_id,
            descripcion=descripcion,
            fecha_limite=fecha_limite,
            completado=completado
        )
        messages.success(request, 'Plazo guardado exitosamente!')
        return redirect('listarPlazos')

def listarPlazos(request):
    plazos = Plazo.objects.all()
    return render(request, 'plazo/listarPlazo.html', {'plazos': plazos})

def editarPlazo(request, id):
    plazo = Plazo.objects.get(id=id)
    proyectos = ProyectoConstruccion.objects.all()
    return render(request, 'plazo/editarPlazo.html', {'plazo': plazo, 'proyectos': proyectos})

def actualizarPlazo(request, id):
    plazo = Plazo.objects.get(id=id)
    plazo.proyecto_id = request.POST['proyecto']
    plazo.descripcion = request.POST['descripcion']
    plazo.fecha_limite = request.POST['fecha_limite']
    plazo.completado = request.POST.get('completado') == 'on'

    plazo.save()
    messages.success(request, 'Plazo editado exitosamente!')
    return redirect('listarPlazos')

def eliminarPlazo(request, id):
    plazo = Plazo.objects.get(id=id)
    plazo.delete()
    messages.success(request, 'Plazo eliminado exitosamente!')
    return redirect('listarPlazos')





