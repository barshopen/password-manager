import React from "react";
import {
  Route,
  BrowserRouter as Router,
  Switch,
  NavLink,
} from "react-router-dom";
import styled from "styled-components";
import Home from "src/Scenarios/Home";
import Contact from "src/Scenarios/Contact";
import About from "src/Scenarios/About";
import Signup from "src/Scenarios/SignUp";
import GlobalStyle from "src/Styles/GlobalStyle";
import * as colors from "src/Styles/Colors";

function App() {
  return (
    <div className="App">
      <GlobalStyle />
      <Router>
        <BodyLayout>
          <Navbar>
            <NavLink to="/" activeClassName="selected">
              Home
            </NavLink>
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

const Navbar = styled.nav`
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  align-items: left;
  justify-content: space-around;

  background-color: #000000;
  border-bottom: 4px solid #ffea00;

  background-color: ${colors.black};

  & a {
    font-weight: bold;
    font-size: 1.2rem;
    padding: 15px;
    color: ${colors.yellow};
    transition: all 0.3s ease-in-out;
  }

  & a:hover {
    background-color: ${colors.yellow};
    color: ${colors.black};
  }
`;
