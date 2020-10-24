import { createGlobalStyle } from "styled-components";
import Breakpoints from "src/Styles/Responsive/Breakpoints";

const GlobalStyle = createGlobalStyle`
    body {
    }
    h1,
    h2{
        font-family: 'Raleway', sans-serif;
        font-weight:400;
    }
    h1{
        color: black;
        @media ${Breakpoints.break1} {   
            font-size: 30rem;
        }
        @media ${Breakpoints.break2}{
            font-size: 38rem   
        }
        @media ${Breakpoints.break3}, ${Breakpoints.break4} {   
            font-size: 50rem;
        }
    }

    h2{
        color:black;
        @media ${Breakpoints.break1} {   
            font-size: 22rem;
        }
        @media ${Breakpoints.break2}{
            font-size: 28rem   
        }
        @media ${Breakpoints.break3}, ${Breakpoints.break4} {   
            font-size: 36rem;
        }

    }

`;

export default GlobalStyle;
