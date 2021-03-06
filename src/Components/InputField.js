import React from "react";
import styled from "styled-components";
import * as colors from "src/Styles/Colors";

export default (props) => {
  function onChangeHandler(e) {
    const val = e.target.value;
    props.onChangeHandler(props.property_name, val);
  }

  return (
    <FloatContainer>
      <input
        type={props.type}
        id={props.property_name}
        placeholder={props.property_label || props.property_name}
        onChange={onChangeHandler}
      />
      <label htmlFor={props.property_name}>
        {props.property_label || props.property_name}
      </label>
    </FloatContainer>
  );
};

const FloatContainer = styled.div`
  position: relative;

  transition: all 0.3s;
  text-transform: capitalize;
  & label {
    font-size: 1em;
    color: #aaa;
    display: block;
    opacity: 1;

    transform: translate(0.5em, -1.5em);
    transform-origin: 0 0;
    transition: all 0.3s;
  }

  & input {
    box-shadow: none;
    background-color: #f5f5f5;
    border-radius: 0px;
    border: solid 1px #ccc;
    border-radius: 2px;

    border-color: #ccc;
    width: 200px;
    transition: all 0.5s ease-in-out;
    padding: 5px;
  }

  & input::placeholder {
    color: transparent;
  }

  & input:focus {
    box-shadow: none;
    outline: none;
    border-color: ${colors.yellow};
  }

  &:focus-within {
    transform: scale(1.05, 1.05);
  }

  & input:focus + label,
  & input:not(:placeholder-shown) + label {
    transform: translateY(-2.8em) scale(0.8);
  }
`;
