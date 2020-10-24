import React from "react";
import {
  Route,
  BrowserRouter as Router,
  Switch,
  NavLink
} from "react-router-dom";
import styled from "styled-components";
import Home from "src/Scenarios/Home";
import Contact from "src/Scenarios/Contact";
import About from "src/Scenarios/About";
import Signup from "src/Scenarios/SignUp";
import NotFound from "src/Scenarios/NotFound"
import GlobalStyle from "src/Styles/GlobalStyle";
import Navbar from "src/Components/Navbar"
function App() {


  return (
    <div className="App">
      <GlobalStyle />
      <Router>
        <BodyLayout>
        <Navbar>
            <NavLink to="/about" activeClassName="selected">
              About
            </NavLink>
            <NavLink to="/contact" activeClassName="selected">
              Contact
            </NavLink>
            <NavLink to="/signup" activeClassName="selected">
              Sign Up
            </NavLink>
        </Navbar>
          <Main>
            <Switch>
              <Route exact path="/" component={Home} />
              <Route exact path="/about" component={About} />
              <Route exact path="/contact" component={Contact} />
              <Route exact path="/signup" component={Signup} />
              <Route component={NotFound} />

            </Switch>
          </Main>

          <footer>foot</footer>
        </BodyLayout>
      </Router>
    </div>
  );
}

export default App;

const BodyLayout = styled.div`
  display: flex;
  flex-direction: column;
  height: 100vh;
`;

const Main = styled.main`
  height: 100vh;
  width: 100vw;

  flex: 1;
  outline: 1px solid black;

  display: flex;
  flex-direction: column;
  align-items: center;
`;

