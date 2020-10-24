import React from 'react';
import styled from 'styled-components';
import * as colors from "src/Styles/Colors";
import {
    NavLink
  } from "react-router-dom";
export default (props) => {
    return <Nav>
    <Logo as={NavLink} to="/" activeClassName="selected">
            Protector
    </Logo>
        {props.children}
    </Nav>
}
const Logo = styled.a`
&&{
    color: ${colors.yellow};
    font-weight:bold;
    font-size:35rem;
    padding: 0;
    
    &&:hover {
    background-color: ${colors.black};
    color: ${colors.yellow};    }
}
`
const Nav = styled.nav`
font-family:"Raleway", Arial, sans-serif;
display: flex;
flex-direction: row;
flex-wrap: wrap;
align-items: left;
justify-content: space-around;

background-color: #000000;
border-bottom: 4px solid #ffea00;

background-color: ${colors.black};

& a {
  font-size: 15rem;
  padding: 15px;
  color: ${colors.yellow};
  transition: all 0.3s ease-in-out;
}

& a:hover {
  background-color: ${colors.yellow};
  color: ${colors.black};
}
`;
