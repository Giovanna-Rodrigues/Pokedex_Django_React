from django.urls import path
from .views import getPokemon, getPokemons, getPokemonsByType, getPokemonsByTypeAndHeight

urlpatterns = [
    path('get_pokemon/', getPokemon, name='get_pokemon'),
    path('get_pokemons/', getPokemons, name='get_pokemons'),
    path('get_pokemons_by_type/', getPokemonsByType, name='get_pokemons_by_type'),
    path('get_pokemons_by_type_and_height/', getPokemonsByTypeAndHeight, name='get_pokemons_by_type_and_height'),
]
