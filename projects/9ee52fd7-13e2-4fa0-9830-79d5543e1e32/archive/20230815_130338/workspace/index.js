require('dotenv').config();
const OAuth2Client = require('./oauth2Client');
const MarketplaceAPI = require('./marketplaceAPI');
const PointOfSaleAPI = require('./pointOfSaleAPI');
const DataMapper = require('./dataMapper');

const marketplaceClient = new OAuth2Client(
  process.env.MARKETPLACE_API_CLIENT_ID,
  process.env.MARKETPLACE_API_CLIENT_SECRET,
  'https://partners.cloudkitchens.com/oauth/token'
);

const pointOfSaleClient = new OAuth2Client(
  process.env.POINT_OF_SALE_API_CLIENT_ID,
  process.env.POINT_OF_SALE_API_CLIENT_SECRET,
  'https://partners.cloudkitchens.com/oauth/token'
);

const marketplaceAPI = new MarketplaceAPI(marketplaceClient, 'https://partners.cloudkitchens.com');
const pointOfSaleAPI = new PointOfSaleAPI(pointOfSaleClient, 'https://partners.cloudkitchens.com');
const dataMapper = new DataMapper();

async function main() {
  const storeId = 'd6cec45b-f9ec-4658-b593-7cd355d86a93';
  const menuData = await marketplaceAPI.getMenu(storeId);
  const mappedData = dataMapper.mapMenuData(menuData);
  await pointOfSaleAPI.upsertMenu(mappedData);
}

main().catch(console.error);
