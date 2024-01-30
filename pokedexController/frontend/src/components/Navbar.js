import React from 'react';
import '../../static/css/Navbar.css';

const Navbar = () => {
  return (
    <nav className="navbar">
      <ul>
        <li><a href=''><img alt="pokeapi-logo" src="./static/image/pngegg.png" className='navbar-img'/></a></li>
        <li className='pages'><a href="/WeightPokemon">Pokemons Weight</a></li>
        <li className='pages'><a href="/GrassPokemon">Grass Pokemons</a></li>
        <li className='pages'><a href="/FlyingPokemon">Flying Pokemons</a></li>
        <li className='pages'><a href="/GuessPokemon">Guess the pokemon</a></li>
      </ul>
    </nav>
  );
};

export default Navbar;