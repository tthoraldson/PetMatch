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
import Preferences from 'views/preferences';
import Home from 'views/home';
import HealthService from 'services/health.service';




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
            path: 'home',
            element: <Home />,
            errorElement: <ErrorPage />,
        },
        {
            path: 'matches',
            element: <Matches />,
            errorElement: <ErrorPage />,
        },
        {
            path: 'preferences',
            element: <Preferences />,
            errorElement: <ErrorPage />,
        }
      ]);
      
      HealthService();
      return (
        <StrictMode>
          <RouterProvider router={router} />
        </StrictMode>
      );
}

  export default App;
