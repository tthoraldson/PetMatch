import { withAuthenticationRequired } from '@auth0/auth0-react';
import Loading from 'components/loading';
import React from 'react';
// import { useLoaderData } from 'react-router-dom';
import Page from '../components/page';

export async function loader() {
  // TODO: Add api call here~
  return 'Hello World';
}

export const Home = () => {
  return (
      <Page title='Home | PetMatch'>
          <h1>PetMatch is NEAT!</h1>
      </Page>
  )
}

export default withAuthenticationRequired(Home, {
  onRedirecting: () => <Loading />,
});