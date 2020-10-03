import React from "react";
import { Route, BrowserRouter as Router, Switch } from "react-router-dom";
import Home from "src/Scenarios/Home";
import Contact from "src/Scenarios/Contact";
import About from "src/Scenarios/About";
import Projects from "src/Scenarios/Projects";

function App() {
  return (
    <div className="App">
      <Router>
        <Switch>
          <Route exact path="/" component={Home} />
          <Route exact path="/about" component={About} />
          <Route exact path="/contact" component={Contact} />
          <Route exact path="/contact" component={Projects} />
        </Switch>
      </Router>
    </div>
  );
}

export default App;
