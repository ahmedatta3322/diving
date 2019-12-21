import React, { Component,Fragment } from 'react'
import ReactDOM from "react-dom"
import Header from "./layout/Header"
import Dashboard from "./divers/Dashboard"
//import Register from "./divers/Register"
export default class App extends Component {
  render() {
    return (
        <Dashboard></Dashboard>
    )
  }
}

  



ReactDOM.render(<App />,document.getElementById("dashboard"));


