import React, { Component } from "react";
import { render } from "react-dom";
import {Navbar} from ".Navbar"

export default class App extends Component {
  constructor(props) {
    super(props);
  }

  render(){
    return <div><Navbar/></div>
  }
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);
