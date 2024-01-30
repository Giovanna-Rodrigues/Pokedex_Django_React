from django.http import JsonResponse
from http import HTTPStatus
from urllib.error import HTTPError
import requests

baseUrlApi = 'https://pokeapi.co/api/v2/'

#Getting an specific pokemon by its name our id.
def getPokemon(namePokemon):
    try:
        url_pokeapi = f"{baseUrlApi}pokemon/{namePokemon}"
        response = requests.get(url_pokeapi)
        response.raise_for_status() 
        dataList = response.json()


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
        print(data)
        return data
    except requests.exceptions.HTTPError as e:
         return {'error': f'Error {e.response.status_code}: {e.response.text}'}

#Getting the first 50 Pokemon
def getPokemons(request):
    params = {'limit': 50}
    apiUrl = f'{baseUrlApi}/pokemon/'
    response = requests.get(apiUrl, params=params)

    if response.status_code == 200:
        data = response.json()
        pokemons = []

        for pokemon in data['results']:
            print(pokemon)
            pokemonData = getPokemon(pokemon['name'])
            pokemons.append(pokemonData)

        print(pokemons)
        return JsonResponse({'pokemons': pokemons})

    else:
        print(response.text)
        return JsonResponse({'error': f'Erro GetPokemons: {response.status_code}'}, status=response.status_code)

#Getting pokemons by Weight
def getPokemonsByWeight(request):
    minWeight = request.GET.get('minWeight')
    maxWeight = request.GET.get('maxWeight')

    apiUrl = f'{baseUrlApi}/pokemon/'
    params = {
        'Weight__gte': minWeight,
        'weight__lte': maxWeight,
    }
    response = requests.get(apiUrl, params=params)

    if response.status_code == 200:
        data = response.json()
        pokemons = []

        for pokemon in data['results']:
            pokemon_data = getPokemon(pokemon['name'])
            pokemons.append(pokemon_data)

        return JsonResponse({'pokemons': pokemons})
    else:
        return JsonResponse({'error': f'Error {response.status_code}'})


#Getting pokemon by the type
def getPokemonsByType(request):
    type_param = request.GET.get('type')
    apiUrl = f'{baseUrlApi}/type/{type_param.lower()}'
    response = requests.get(apiUrl)

    if response.status_code == 200:
        data = response.json()
        pokemons = []

        for pokemon in data['pokemon']:
            pokemonData = getPokemon(pokemon['pokemon']['name'])
            pokemons.append(pokemonData)

        return JsonResponse({'pokemons': pokemons})

    else:
        print(response.text)
        return JsonResponse({'error': f'Error {response.status_code}'}, status=response.status_code)

#Getting pokemon by the type and Height
def getPokemonsByTypeAndHeight(request):
    type = (request.GET.get('type')).lower()
    minHeight = request.GET.get('minHeight')

    apiUrl = f'{baseUrlApi}/pokemon/'
    params = {
        'types': type,
        'Height__gte': minHeight,
    }
    response = requests.get(apiUrl, params=params)

    if response.status_code == 200:
        data = response.json()
        pokemons = []

        for pokemon in data['results']:
            pokemon_data = getPokemon(pokemon['name'])
            pokemons.append(pokemon_data)

        return JsonResponse({'pokemons': pokemons})
    else:
        return JsonResponse({'error': f'Error {response.status_code}'})

