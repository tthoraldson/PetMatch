import React from 'react';
import LoginButton from 'utils/login';
import PetImage from 'utils/petImage';
import Page from '../components/page';

export async function loader() {
    // TODO: Add api call here~
    return 'Hello World';
  }
  
function Landing() {
    return (
        <Page title='PetMatch'>
            <h1>PetMatch</h1>
            <h3>PetMatch helps you find your dream pet</h3>
            <div><LoginButton/></div>
            <p>Join the PetMatch community and be a hero to furry friends in need. By signing up, you'll have the opportunity to adopt a loving cat or dog who's eagerly waiting for a forever home. Give them a chance at happiness and help save their life today. The love and joy they'll bring to your life is immeasurable. What are you waiting for? Sign up now and give a pet a second chance at love!</p>
            <PetImage image_url='https://images.unsplash.com/photo-1529778873920-4da4926a72c2?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1336&q=80'/>
        </Page>

    )
}

export default Landing;