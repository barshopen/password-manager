import React, { useState } from "react";
import styled from "styled-components";
import Container from "src/Components/Container";
import InputField from "src/Components/InputField";

const formState = {};
export default () => {
  const [form, setForm] = useState(formState);

  function handleSubmit(event) {
    event.preventDefault();
    const f = new FormData();
    Object.keys(form).forEach(k=>f.append(k,form[k]));
    
    window.fetch('/api/login', {
      method: 'POST',
      headers: {
        delay: 1500,
            },
      body: f,
    }).then(res=>{console.log("Request", res)}, err=>{console.log("error", err)})
  }

  function onChangeHandler(property, val) {
    setForm((prevForm) => ({ ...prevForm, [property]: val }));
    console.log(form);
  }

  return (
    <Container>
      <form onSubmit={handleSubmit}>
        <InputField property_name="email" onChangeHandler={onChangeHandler} />
        
        <InputField
          property_label="password"
          property_name="password"
          type="password"
          onChangeHandler={onChangeHandler}
        />

        <Submit type="submit" value="Submit" />
      </form>
    </Container>
  );
};

const Submit = styled.input`
  display: flex;
  justify-content: center;
  align-items: center;

  width: 150px;
  height: 30px;
  border-radius: 3px;
  border: none;
  box-shadow: none;


  padding: 10px 20px;
  min-height: 34px;
  background-color: #008941;
  box-shadow: none;
  color: #fff;
  font-size: 14px;
  font-weight: 700;
  text-transform: none;
`;
