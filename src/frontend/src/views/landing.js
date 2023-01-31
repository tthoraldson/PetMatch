import React from 'react';
import LoginButton from 'utils/login';
import LogoutButton from 'utils/logout';
import PetImage from 'utils/petImage';
import Page from '../components/page';

export async function loader() {
    // TODO: Add api call here~
    return 'Hello World';
  }
  
function Landing() {
    // Welcome to Petmatch!

    // Slogan

    // Cute cat photo

    // Login/signup
    return (
        <Page title='PetMatch'>
            <h1>PetMatch helps you find your dream pet</h1>
            <div><LoginButton/></div>
            <PetImage image_url='https://images.unsplash.com/photo-1529778873920-4da4926a72c2?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1336&q=80'/>
        </Page>

    )
}

export default Landing;