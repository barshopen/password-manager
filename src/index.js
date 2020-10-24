import React from "react";
import ReactDOM from "react-dom";
import App from "src/App";
import * as serviceWorker from "src/serviceWorker";
import { Normalize } from "styled-normalize";
import LocalRest from "src/Styles/LocalReset";
import Typography from "src/Styles/Typography";
import GlobalStyle from "src/Styles/GlobalStyle";

ReactDOM.render(
  <React.StrictMode>
    <LocalRest />
    <Typography />
    <Normalize />
    <GlobalStyle />
    <App />
  </React.StrictMode>,
  document.getElementById("root")
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
