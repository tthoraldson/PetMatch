import React from 'react';
import { useLoaderData } from 'react-router-dom';
import Page from '../page';

export async function loader() {
  // TODO: Add api call here~
  return 'Hello World';
}

export default function Home() {
  const data = useLoaderData();

  return (
    <Page title="Home">
      <h1>{data}</h1>
    </Page>
  );
}
