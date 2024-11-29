# capa de vista/presentación

from django.shortcuts import redirect, render
from app.layers.services.services import getAllImages #se completan los campos que faltaban y se importa la funcion correspondiente
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from app.layers.transport.transport import fetch_characters

def index_page(request):
    return render(request, 'index.html')

# esta función obtiene 2 listados que corresponden a las imágenes de la API y los favoritos del usuario, y los usa para dibujar el correspondiente template.
# si el opcional de favoritos no está desarrollado, devuelve un listado vacío.
def home(request):
    # Llamamos a getAllImages para obtener las imágenes.
    images = getAllImages()

    # Si tienes un parámetro de búsqueda (input), asegúrate de pasarlo a la vista.
    search_input = request.GET.get('search', None)

    # También puedes pasar los favoritos si es necesario.
    favourite_list = []

    return render(request, 'home.html', {'images': images, 'favourite_list': favourite_list, 'search_input': search_input})

def search(request):
    search_msg = request.POST.get('query', '')

    # si el texto ingresado no es vacío, trae las imágenes y favoritos desde services.py,
    # y luego renderiza el template (similar a home).
    if (search_msg != ''):
        pass
    else:
        return redirect('home')


# Estas funciones se usan cuando el usuario está logueado en la aplicación.
@login_required
def getAllFavouritesByUser(request):
    favourite_list = []
    return render(request, 'favourites.html', { 'favourite_list': favourite_list })

@login_required
def saveFavourite(request):
    pass

@login_required
def deleteFavourite(request):
    pass

@login_required
def exit(request):
    pass