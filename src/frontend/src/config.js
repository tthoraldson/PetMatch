export function getConfig() {
  const audience = null;

  const domain = process.env.REACT_APP_AUTH0_DOMAIN;
  const clientId = process.env.REACT_APP_AUTH0_CLIENTID;

  return {
    domain: domain,
    clientId: clientId,
    ...(audience ? { audience } : null),
  };
}