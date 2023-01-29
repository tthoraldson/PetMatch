import React from 'react';
import Page from '../components/page';

export async function loader() {
    // TODO: Add api call here~
    return 'Hello World';
  }
  
function Landing() {
    return (
        <Page title='PetMatch'>
            <h1>Hello!</h1>
        </Page>
    )
}

export default Landing;