import { createGlobalStyle } from "styled-components";

const Typography = createGlobalStyle`
html {
    font-size: 1px;
  }
  body {
    margin: 0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Roboto", "Oxygen",
      "Ubuntu", "Cantarell", "Fira Sans", "Droid Sans", "Helvetica Neue",
      sans-serif;
    font-size: 16rem;
    font-weight: 400;
    line-height: 1.3;
    color: #222;
  }

`;

export default Typography;
