import React from 'react';
import Page from '../components/page';

export async function loader() {
    //'http://localhost:8086/'
    console.log(process.env.API_URL)
    fetch(process.env.API_URL)
      .then((response) => response.json())
      .then((data) => {
         console.log(data);
      })
      .catch((err) => {
         console.log(err.message);
      });
  }

function About() {
    loader();

    return (
        <Page title='About | Petmatch'>
            <h1>About</h1>
        </Page>
    )
}

export default About;