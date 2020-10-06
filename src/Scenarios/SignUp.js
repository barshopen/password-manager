import React from "react";
import styled from "styled-components";
import Container from "src/Components/Container";
import InputField from "src/Components/InputField";

export default () => {
  return (
    <Container>
      <form>
        <InputField property_name="Name" />
        <InputField property_name="Last Name" />

        <InputField property_name="Email" type="Email" />

        <InputField property_name="Password" type="password" />
        <InputField property_name="Confirm Password" type="password" />
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
