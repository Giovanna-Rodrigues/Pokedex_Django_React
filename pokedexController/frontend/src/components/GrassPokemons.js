import React, { useEffect, useState } from "react";
import Pokemon from "./Pokemon"; 
import "../../static/css/Pokedex.css";

const GrassPokemon = () => {
    const [pokemons, setPokemons] = useState([]);
  
    useEffect(() => {
      const fetchData = async () => {
        try {
          const response = await fetch("api/get_pokemons_by_type/?type=grass");
          const data = await response.json();
          setPokemons(data.pokemons);
        } catch (error) {
          console.error("Erro ao obter dados da API:", error);
        }
      };
  
      fetchData();
    }, []);
  
    return (
      <div>
        <h3>All type “Grass” Pokemon</h3>
        <div className="pokedex-component">
          {pokemons.map((pokemon) => (
            <Pokemon key={pokemon.name} pokemon={pokemon} />
          ))}
        </div>  
      </div>
    );
};

export default GrassPokemon;
