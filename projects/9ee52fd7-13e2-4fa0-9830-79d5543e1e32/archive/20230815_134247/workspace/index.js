const OAuth2Client = require('./OAuth2Client');
const ApiRequest = require('./ApiRequest');
const DataMapper = require('./DataMapper');
const Workflow = require('./Workflow');

async function main() {
  const marketplaceClient = new OAuth2Client(
    process.env.MARKETPLACE_CLIENT_ID,
    process.env.MARKETPLACE_CLIENT_SECRET,
    'https://partners.cloudkitchens.com/oauth/token'
  );

  const posClient = new OAuth2Client(
    process.env.POS_CLIENT_ID,
    process.env.POS_CLIENT_SECRET,
    'https://partners.cloudkitchens.com/oauth/token'
  );

  const getMenuRequest = new ApiRequest(
    marketplaceClient,
    'https://partners.cloudkitchens.com/api/menus'
  );

  const upsertMenuRequest = new ApiRequest(
    posClient,
    'https://partners.cloudkitchens.com/api/menus'
  );

  const dataMapper = new DataMapper();

  const workflow = new Workflow(getMenuRequest, upsertMenuRequest, dataMapper);

  await workflow.run();
}

main().catch(console.error);
