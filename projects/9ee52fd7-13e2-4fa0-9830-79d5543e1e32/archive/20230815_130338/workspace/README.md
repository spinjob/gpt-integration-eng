Based on the provided information, we will need to create a Node.js application that integrates two APIs using OAuth2 authentication. The application will have two main steps: 

1. Fetching a menu from the first API (Marketplace API)
2. Updating the menu on the second API (Point-of-Sale API) with the fetched data.

We will need the following core classes and functions:

1. `OAuth2Client`: This class will handle the OAuth2 authentication for both APIs. It will have methods for getting and refreshing access tokens.
2. `MarketplaceAPI`: This class will handle interactions with the Marketplace API. It will have a method `getMenu` for fetching the menu.
3. `PointOfSaleAPI`: This class will handle interactions with the Point-of-Sale API. It will have a method `upsertMenu` for updating the menu.
4. `DataMapper`: This class will handle the mapping of data between the two APIs. It will have a method `mapMenuData` for mapping the menu data from the Marketplace API to the format required by the Point-of-Sale API.
5. `main`: This function will orchestrate the whole process. It will call the necessary methods from the above classes to fetch the menu from the Marketplace API, map the data, and update the menu on the Point-of-Sale API.

Now, let's implement these classes and functions.

First, we will create a `package.json` file to define our Node.js project and its dependencies.

package.json
