import React from 'react';
import { useLoaderData } from 'react-router-dom';
import Page from '../components/page';

export async function loader() {
  // TODO: Add api call here~
  return 'Hello World';
}

function Home() {
  return (
      <Page>
          <h1>PetMatch is NEAT!</h1>
      </Page>
  )
}

export default Home;