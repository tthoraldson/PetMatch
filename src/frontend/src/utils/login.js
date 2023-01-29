import React from "react";
import { useAuth0 } from "@auth0/auth0-react";

const LoginButton = () => {
  const { loginWithRedirect } = useAuth0();

  return <button onClick={() => loginWithRedirect({
    authorizationParams: {
        redirect_uri: 'http://localhost:3000/matches'
      }
  })}>Log In</button>;
};

export default LoginButton;