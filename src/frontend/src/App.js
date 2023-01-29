import React, { StrictMode } from 'react';
import './index.css';
import ErrorPage from './views/errorpage';
import About from './views/about';
import Landing from './views/landing';

import {
  createBrowserRouter, RouterProvider,
} from "react-router-dom";
import { useAuth0 } from '@auth0/auth0-react';
import Matches from 'views/matches';



const App = () => {
    const { error } = useAuth0();
  
    if (error) {
      return <div>Oops... {error.message}</div>;
    }
  
    const router = createBrowserRouter([
        {
          path: '/',
          element: <Landing />,
          errorElement: <ErrorPage />,
          //loader: homeLoader,
        },
        {
          path: 'about',
          element: <About />,
          errorElement: <ErrorPage />,
          //loader: postLoader,
        },
        {
            path: 'matches',
            element: <Matches />,
            errorElement: <ErrorPage />,
        }
      ]);
      
      return (
        <StrictMode>
          <RouterProvider router={router} />
        </StrictMode>
      );
}

  export default App;
