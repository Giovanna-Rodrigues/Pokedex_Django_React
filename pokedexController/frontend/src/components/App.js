// App.js
import React from "react";
import { BrowserRouter as Router, Route, Switch} from "react-router-dom";
import Navbar from "./Navbar";
import Pokedex from "./Pokedex";
import WeightPokemon from "./WeightPokemon";
import GrassPokemon from "./GrassPokemons";
import FlyingPokemon from "./FlyingPokemon";

const App = () => {
  return (
    <Router>
      <div>
        <Navbar />
        <Router>
          <Switch>
            <Route exact path="/" component={Pokedex} />
            <Route path="/WeightPokemon" component={WeightPokemon} />
            <Route path="/GrassPokemon" component={GrassPokemon} />
            <Route path="/FlyingPokemon" component={FlyingPokemon} />
          </Switch>
        </Router>
      </div>
    </Router>
  );
};

export default App;
