import { useAuth0, withAuthenticationRequired } from '@auth0/auth0-react';
import Loading from 'components/loading';
import React from 'react';
import Page from '../components/page';

export async function loader() {
    // TODO: Add api call here~
    return 'Hello World';
  }
  
export const Matches = () => {
    const { user } = useAuth0();
    console.warn(user);
    
    return (
        <Page title='Matches | Petmatch'>
            <h1>Matches</h1>
        </Page>
    )
}


export default withAuthenticationRequired(Matches, {
    onRedirecting: () => <Loading />,
  });