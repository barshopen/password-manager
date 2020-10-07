import React, { useState } from "react";
import styled from "styled-components";
import Container from "src/Components/Container";
import InputField from "src/Components/InputField";

const formState = {
  Name: "",
  Email: "",
  password: "",
  confirm_password: "",
};
export default () => {
  const [form, setForm] = useState(formState);

  function handleSubmit(event) {
    event.preventDefault();
    console.log(form);
  }

  function onChangeHandler(property, val) {
    setForm((prevForm) => ({ ...prevForm, [property]: val }));
    console.log(form);
  }

  return (
    <Container>
      <form onSubmit={handleSubmit}>
        <InputField property_name="name" onChangeHandler={onChangeHandler} />
        <InputField
          property_name="email"
          type="Email"
          onChangeHandler={onChangeHandler}
        />

        <InputField
          property_name="password"
          type="password"
          onChangeHandler={onChangeHandler}
        />
        <InputField
          property_name="confirm_password"
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
  background: dodgerblue;
  border-radius: 6px;
  border: none;
`;
