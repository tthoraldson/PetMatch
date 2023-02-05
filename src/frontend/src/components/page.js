import React, { Fragment, useEffect } from 'react';
import Navigation from './navigation';

export default function Page(props) {
  useEffect(() => {
    document.title = props.title;
  }, [props.title]);

  return (
    <Fragment>
      <Navigation />
      <main>{props.children}</main>
    </Fragment>
  );
}