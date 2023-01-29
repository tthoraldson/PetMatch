import React from 'react';
import LoginButton from 'utils/login';
import LogoutButton from 'utils/logout';
import Page from '../components/page';

export async function loader() {
    // TODO: Add api call here~
    return 'Hello World';
  }
  
function Landing() {
    return (
        <Page title='PetMatch'>
            <h1>Hello!</h1>
            <LoginButton/>
            <LogoutButton/>
        </Page>
    )
}

export default Landing;