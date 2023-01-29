import React from 'react';
import { useRouteError } from 'react-router-dom';
import Page from '../components/page';

export default function ErrorPage() {
  const error = useRouteError();

  let message;

  // @ts-ignore
  if (error.status === 404) {
    message = <p>There's nothing here.</p>;
  // @ts-ignore
  } else if (error.status === 500) {
    message = <p>There was a problem fetching the data for this page.</p>;
  } else {
    message = <p>An unexpected error occurred.</p>;
  }

  // @ts-ignore
  return <Page title={error.statusText ?? 'Error'}>{message}</Page>;
}