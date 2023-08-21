const axios = require('axios');

class PointOfSaleAPI {
  constructor(oauth2Client, baseUrl) {
    this.oauth2Client = oauth2Client;
    this.baseUrl = baseUrl;
  }

  async upsertMenu(menuData) {
    const accessToken = await this.oauth2Client.getAccessToken();
    await axios.post(`${this.baseUrl}/menu`, menuData, {
      headers: {
        'Authorization': `Bearer ${accessToken}`
      }
    });
  }
}

module.exports = PointOfSaleAPI;
