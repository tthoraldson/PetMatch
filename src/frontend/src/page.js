import React, { Fragment, useEffect } from 'react';
import Navigation from './components/navigation';

export default function Page(props) {
  useEffect(() => {
    document.title = props.title;
  }, [props.title]);

  return (
    <Fragment>
      <Navigation />
        <h1>{props.title}</h1>
      <main>{props.children}</main>
    </Fragment>
  );
}