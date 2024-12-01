# translator: se refiere a un componente o conjunto de funciones que se utiliza para convertir o "mapear" datos de un formato o estructura a otro. Esta conversión se realiza típicamente cuando se trabaja con diferentes capas de una aplicación, como por ejemplo, entre la capa de datos y la capa de presentación, o entre dos modelos de datos diferentes.
import requests
from app.layers.utilities.card import Card

# usado cuando la info. viene de la API, para transformarla en una Card.
def fromRequestIntoCard(object):
    episode_url = object.get('episode', [])[0] if object.get('episode') else None 
    episode_name = None 

    if episode_url: 
        episode_response = requests.get(episode_url) 
        if episode_response.status_code == 200: 
            episode_data = episode_response.json() 
            episode_name = episode_data.get('name')
    card = Card(
                        url=object['image'],
                        name=object['name'],
                        status=object['status'], 
                        last_location = object['location']['name'],
                        first_seen = episode_name
                )
    return card

# usado cuando la info. viene del template, para transformarlo en una Card antes de guardarlo en la base de datos.
def fromTemplateIntoCard(templ): 
    card = Card(
                        url=templ.POST.get("url"),
                        name=templ.POST.get("name"),
                        status=templ.POST.get("status"),
                        last_location=templ.POST.get("last_location"),
                        first_seen=templ.POST.get("first_seen")
                )
    return card

# cuando la info. viene de la base de datos, para transformarlo en una Card antes de mostrarlo.
def fromRepositoryIntoCard(repo_dict):
    card = Card(
                        id=repo_dict['id'],
                        url=repo_dict['url'],
                        name=repo_dict['name'],
                        status=repo_dict['status'],
                        last_location=repo_dict['last_location'],
                        first_seen=repo_dict['first_seen'],
                )
    return card