const axios = require('axios');

class ApiRequest {
  constructor(oauth2Client, url) {
    this.oauth2Client = oauth2Client;
    this.url = url;
  }

  async send(method, data) {
    const token = await this.oauth2Client.getAccessToken();

    const response = await axios({
      method,
      url: this.url,
      headers: {
        Authorization: `Bearer ${token}`
      },
      data
    });

    return response.data;
  }
}

module.exports = ApiRequest;
