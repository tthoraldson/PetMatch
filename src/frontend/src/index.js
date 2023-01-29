import React from "react";
import "./index.css";
import App from "./app";
import { Auth0Provider } from "@auth0/auth0-react";
import { getConfig } from "./config";
import { createRoot } from "react-dom/client";

// Please see https://auth0.github.io/auth0-react/interfaces/Auth0ProviderOptions.html
// for a full list of the available properties on the provider
const config = getConfig();

const providerConfig = {
  domain: config.domain,
  clientId: config.clientId,
  authorizationParams: {
    redirect_uri: window.location.origin,
    ...(config.audience ? { audience: config.audience } : null),
  },
};


const container = document.getElementById('root');
const root = createRoot(container);

root.render(
  <Auth0Provider {...providerConfig}>
    <App />
  </Auth0Provider>,
);