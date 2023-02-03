var configJson = {};

// TODO: This is horrid, deal with it
if (process.env.REACT_APP_AUTH0_DOMAIN == null) {
  // @ts-ignore
  configJson = require("./auth_config.json");
}



export function getConfig() {
  const audience = null;

  const domain = process.env.REACT_APP_AUTH0_DOMAIN || configJson.domain;
  const clientId = process.env.REACT_APP_AUTH0_CLIENTID || configJson.domain;

  return {
    domain: domain,
    clientId: clientId,
    ...(audience ? { audience } : null),
  };
}