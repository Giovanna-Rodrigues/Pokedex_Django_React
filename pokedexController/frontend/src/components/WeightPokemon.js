// Pokedex.jsx
import React, { useEffect, useState } from "react";
import Pokemon from "./Pokemon"; 
import "../../static/css/Pokedex.css";

const WeightPokemon = () => {
    const [pokemons, setPokemons] = useState([]);
  
    useEffect(() => {
      const fetchData = async () => {
        try {
          const response = await fetch("api/get_pokemons_by_weight/?minWeight=30&maxWeight=80");
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
        <h3>All Pokemon that weight more than 30 and less than 80</h3>
        <div className="pokedex-component">
          {pokemons.map((pokemon) => (
            <Pokemon key={pokemon.name} pokemon={pokemon} />
          ))}
        </div>  
      </div>
    );
};

export default WeightPokemon;
