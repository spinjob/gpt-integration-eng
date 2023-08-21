const axios = require('axios');

class OAuth2Client {
  constructor(clientId, clientSecret, tokenUrl) {
    this.clientId = clientId;
    this.clientSecret = clientSecret;
    this.tokenUrl = tokenUrl;
    this.token = null;
  }

  async getAccessToken() {
    if (!this.token) {
      const response = await axios.post(this.tokenUrl, {
        client_id: this.clientId,
        client_secret: this.clientSecret,
        grant_type: 'client_credentials'
      });

      this.token = response.data.access_token;
    }

    return this.token;
  }
}

module.exports = OAuth2Client;
