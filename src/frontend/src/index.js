import React, { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import './index.css';
import Home from './views/home';
import ErrorPage from './views/errorpage';
import About from './views/about';
// import { Auth0Provider } from "@auth0/auth0-react";

import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";

const container = document.getElementById('root');
const root = createRoot(container);

const router = createBrowserRouter([
  {
    path: '/',
    element: <Home />,
    errorElement: <ErrorPage />,
    //loader: homeLoader,
  },
  {
    path: 'about',
    element: <About />,
    errorElement: <ErrorPage />,
    //loader: postLoader,
  },
]);

root.render(
  <StrictMode>
    <RouterProvider router={router} />
  </StrictMode>
);

