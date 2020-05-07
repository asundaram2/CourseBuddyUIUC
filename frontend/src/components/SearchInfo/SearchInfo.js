import React from "react";

import Container from "react-bootstrap/Container";
import Navbar from "react-bootstrap/Navbar";
import SearchInfoSection from "../SearchInfoSection/SearchInfoSection";

function SearchInfo(props) {
  function displaySection(section) {
    console.log(props.crn, section)
    return <SearchInfoSection key = {props.crn} section={section} username={props.username} />;
  }

  return (
    <Container className="p-0" fluid={true}>
    <br />
      <div>{JSON.parse(props.results).map(displaySection)}</div>
    </Container>
  );
}

export default SearchInfo;
