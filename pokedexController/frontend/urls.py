from django.urls import path
from .views import index

urlpatterns = [
    path('',index),
    path('WeightPokemon',index),
    path('GrassPokemon',index),
    path('FlyingPokemon',index),
    path('GrassPokemon',index),
]