import React, { Component } from "react";
import { createRoot } from 'react-dom/client';
import { BrowserRouter as Router, Switch, Route } from "react-router-dom"; // Importe o Switch e o Route
import Navbar from "./Navbar.js"
import Pokedex from "./Pokedex.js";
import WeightPokemon from "./WeightPokemon.js"
import GrassPokemon from "./GrassPokemons.js";
import FlyingPokemon from "./FlyingPokemon.js"

export default class App extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <Router> {/* Adicione o Router envolvendo o conteúdo */}
        <div>
          <div><Navbar /></div>
          <Switch>
            <Route path="/" exact component={Pokedex} />
            <Route path="/WeightPokemon" component={WeightPokemon} />
            <Route path="/GrassPokemon" component={GrassPokemon} />
            <Route path="/FlyingPokemon" component={FlyingPokemon} />
          </Switch>
        </div>
      </Router>
    );
  }
}

const appDiv = document.getElementById("app");
createRoot(appDiv).render(<App />);
