import { withAuthenticationRequired } from '@auth0/auth0-react';
import Box from '@mui/material/Box';
import Loading from 'components/loading';
import React from 'react';
import PetImage from 'utils/petImage';
// import { useLoaderData } from 'react-router-dom';
import Page from '../components/page';

export async function loader() {
  // TODO: Add api call here~
  return 'Hello World';


    // get user preferences
    // set user preferences

      // get new pet
}

export async function getNewPet(){
  // grab cat/dog preference
}

export async function savePreference(){
  
}

export const Home = () => {
  return (
      <Page title='Home | PetMatch'>
          <Box
          sx={{
            width: 500,
            height: 500,
          }}>
            <PetImage image_url='https://images.unsplash.com/photo-1529778873920-4da4926a72c2?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1336&q=80'/>
          </Box>
      </Page>
  )
}

export default withAuthenticationRequired(Home, {
  onRedirecting: () => <Loading />,
});