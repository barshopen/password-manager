import { createGlobalStyle } from "styled-components";

export const GlobalStyle = createGlobalStyle`

body{
  font-family: 'Lato', sans-serif;
  height: 100%;
}

h1, h2{
  font-family: 'Roboto', sans-serif;
}

h1{
  font-size: 4rem;
}

h2{
  font-size: 2rem;
}

a{
    text-decoration: none;
}
`;

export default GlobalStyle;
