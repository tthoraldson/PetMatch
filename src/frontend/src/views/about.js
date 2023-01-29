import React from 'react';
import Page from '../components/page';

export async function loader() {
    // TODO: Add api call here~
    return 'Hello World';
  }
  
function About() {
    return (
        <Page title='About | Petmatch'>
            <h1>About</h1>
        </Page>
    )
}

export default About;