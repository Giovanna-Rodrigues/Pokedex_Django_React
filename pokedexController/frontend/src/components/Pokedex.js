import React, { useEffect, useState } from "react";
import Pokemon from "./Pokemon"; 
import "../../static/css/Pokedex.css";

const Pokedex = () => {
    const [pokemons, setPokemons] = useState([]);
  
    useEffect(() => {
      const fetchData = async () => {
        try {
          const response = await fetch("api/get_pokemons/");
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
        <div className="pokedex-component">
          {pokemons.map((pokemon) => (
            <Pokemon key={pokemon.name} pokemon={pokemon} />
          ))}
        </div>  
      </div>
    );
};

export default Pokedex;
