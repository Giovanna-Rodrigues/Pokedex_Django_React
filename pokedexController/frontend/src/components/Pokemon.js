import React from "react";
import '../../static/css/Pokemon.css';

const Pokemon = (props) => {
    const { pokemon } = props;
    const { number, name, height, weight, sprite, types } = pokemon;

    return (
        <div className="pokemon-component">
            <img src={sprite} alt={name} className="pokemon-image" />
            <h3 className="pokemon-title">{number} - {name}</h3>
            <p>Type: {types.join(', ')}</p>
            <p>Height: {height}</p>
            <p>Weight: {weight}</p>
        </div>
    );
}

export default Pokemon;
