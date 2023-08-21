const axios = require('axios');

class OAuth2Client {
  constructor(clientId, clientSecret, tokenUrl) {
    this.clientId = clientId;
    this.clientSecret = clientSecret;
    this.tokenUrl = tokenUrl;
    this.accessToken = null;
    this.refreshToken = null;
  }

  async getAccessToken() {
    if (!this.accessToken) {
      await this.refreshAccessToken();
    }
    return this.accessToken;
  }

  async refreshAccessToken() {
    const response = await axios.post(this.tokenUrl, {
      client_id: this.clientId,
      client_secret: this.clientSecret,
      grant_type: 'client_credentials'
    });
    this.accessToken = response.data.access_token;
    this.refreshToken = response.data.refresh_token;
  }
}

module.exports = OAuth2Client;
