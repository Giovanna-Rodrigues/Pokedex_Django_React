import React from 'react';
import './Navbar.css';

const Navbar = () => {
  return (
    <nav className="navbar">
      <ul>
        <li><img alt="pokeapi-logo" src="./static/image/pokedex-logo.png" className='navbar-img'/></li>
        <li><a href="#">opção 1</a></li>
        <li><a href="#">opção 2</a></li>
        <li><a href="#">opção 3</a></li>
        <li><a href="#">opção 4</a></li>
      </ul>
    </nav>
  );
};

export default Navbar;