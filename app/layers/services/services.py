# capa de servicio/lógica de negocio

import requests
from app.layers.persistence import repositories
from app.layers.utilities.translator import fromRequestIntoCard
from django.contrib.auth import get_user
from app.layers.transport.transport import fetch_characters
from app.layers.utilities.card import Card # Importa la clase Card desde card.py

def fromRequestIntoCard(json_data):
    episode_url = json_data.get('episode', [])[0] if json_data.get('episode') else None 
    episode_name = None 
    
    if episode_url: 
        episode_response = requests.get(episode_url) 
        if episode_response.status_code == 200: 
            episode_data = episode_response.json() 
            episode_name = episode_data.get('name')
        else: 
            print(f"Error fetching episode data: {episode_response.status_code}") 
    print(f"Episodio URL: {episode_url}, Nombre del episodio: {episode_name}")

    return Card(
        name=json_data.get('name'),
        url=json_data.get('image'),
        status=json_data.get('status'),
        last_location=json_data.get('location', {}).get('name'),
        first_seen=episode_name
    )

def getAllImages(input=None):
    # obtiene un listado de datos "crudos" desde la API, usando a transport.py.
    json_collection = fetch_characters()

    # recorre cada dato crudo de la colección anterior, lo convierte en una Card y lo agrega a images.
    images = []
    for json_data in json_collection:
        card = fromRequestIntoCard(json_data)
        if input is None or input.lower() in card.name.lower():
            images.append(card)

    return images

# añadir favoritos (usado desde el template 'home.html')
def saveFavourite(request):
   fav = fromRequestIntoCard # transformamos un request del template en una Card.
   fav.user = get_user # le asignamos el usuario correspondiente.

   return repositories.saveFavourite(fav) # lo guardamos en la base.


# usados desde el template 'favourites.html'
def getAllFavourites(request):
    if not request.user.is_authenticated:
        return []
    else:
        user = get_user(request)

        favourite_list = [] # buscamos desde el repositories.py TODOS los favoritos del usuario (variable 'user').
        mapped_favourites = []

        for favourite in favourite_list:
            card = '' # transformamos cada favorito en una Card, y lo almacenamos en card.
            mapped_favourites.append(card)

        return mapped_favourites

def deleteFavourite(request):
    favId = request.POST.get('id')
    return repositories.deleteFavourite(favId) # borramos un favorito por su ID.


