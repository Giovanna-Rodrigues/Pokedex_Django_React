from django.http import JsonResponse
import urllib.request
import json
from http import HTTPStatus
from urllib.error import HTTPError
import requests

baseUrlApi = 'https://pokeapi.co/api/v2/pokemon/'

#Getting an specific pokemon by its name our id.
def getPokemon(request):
    if request.method == 'POST':
        pokemon = request.POST['pokemon'].lower()
        pokemon = pokemon.replace(' ', '%20')

        url_pokeapi = urllib.request.Request(baseUrlApi + pokemon)
        url_pokeapi.add_header('User', "user")

        try:
            source = urllib.request.urlopen(url_pokeapi).read()
            dataList = json.loads(source)

            # Converting height and weight
            heightObtained = (float(dataList['height']) * 0.1)
            heightRounded = round(heightObtained, 2)
            weightObtained = (float(dataList['weight']) * 0.1)
            weightRounded = round(weightObtained, 2)

            # Extracting types
            types = [entry['type']['name'] for entry in dataList['types']]

            data = {
                "number": str(dataList['id']),
                "name": str(dataList['name']).capitalize(),
                "types": types,
                "height": str(heightRounded) + " m",
                "weight": str(weightRounded) + " kg",
                "sprite": str(dataList['sprites']['versions']['generation-v']['black-white']['front_default']),
            }

            return JsonResponse(data)
        except urllib.error.HTTPError as e:
            return JsonResponse({'error': f'Error {e.code}'})
    else:
        return JsonResponse({'error': 'Invalid request method'})

#Getting the first 50 Pokemon
def getPokemons(request):
    params = {'limit': 50}
    response = requests.get(baseUrlApi, params=params)

    if response.status_code == 200:
        data = response.json()
        pokemons = []

        for pokemon in data['results']:
            pokemonData = getPokemon(pokemon['name'])
            pokemons.append(pokemonData)

        return JsonResponse({'pokemons': pokemons})

    else:
        return JsonResponse({'error': f'ErroapiUrlr {response.status_code}'})

#Getting pokemon by the type
def getPokemonsByType(request, type):
    apiUrl = baseUrlApi + type.lower() 
    response = requests.get(apiUrl)

    if response.status_code == 200:
        data = response.json()
        pokemons = []

        pokemon_list = [pokemon['pokemon']['name'] for pokemon in data['pokemon']]
        for pokemon in pokemon_list:
            pokemonData = getPokemon(pokemon['name'])
            pokemons.append(pokemonData)

        return JsonResponse({'pokemons': pokemons})
    else:
        return JsonResponse({'error': f'Error {response.status_code}'})

#Getting pokemon by the type and Height
def getPokemonsByTypeAndHeight(request, type):
    apiUrl = baseUrlApi + type.lower()
    response = requests.get(apiUrl)

    if response.status_code == 200:
        data = response.json()
        pokemons = []

        pokemon_list = [pokemon['pokemon']['name'] for pokemon in data['pokemon']]
        for pokemon_name in pokemon_list:
            pokemon_data = getPokemon(pokemon_name)

            # Verifying height
            if pokemon_data.get('height', 0) > 10:
                pokemons.append(pokemon_data)

        return JsonResponse({'pokemons': pokemons})
    else:
        return JsonResponse({'error': f'Error {response.status_code}'})

