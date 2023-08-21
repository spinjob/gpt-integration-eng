const axios = require('axios');

class MarketplaceAPI {
  constructor(oauth2Client, baseUrl) {
    this.oauth2Client = oauth2Client;
    this.baseUrl = baseUrl;
  }

  async getMenu(storeId) {
    const accessToken = await this.oauth2Client.getAccessToken();
    const response = await axios.get(`${this.baseUrl}/menu`, {
      headers: {
        'Authorization': `Bearer ${accessToken}`,
        'X-Store-Id': storeId
      }
    });
    return response.data;
  }
}

module.exports = MarketplaceAPI;
