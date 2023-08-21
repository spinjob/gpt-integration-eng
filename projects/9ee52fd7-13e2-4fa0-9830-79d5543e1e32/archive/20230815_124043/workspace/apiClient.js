const axios = require('axios');
const jwt = require('jsonwebtoken');

class APIClient {
  constructor(baseURL, clientId, clientSecret) {
    this.baseURL = baseURL;
    this.clientId = clientId;
    this.clientSecret = clientSecret;
    this.token = null;
  }

  async authenticate() {
    const payload = {
      iss: this.clientId,
      aud: this.baseURL,
      exp: Math.floor(Date.now() / 1000) + 60 * 60 // 1 hour from now
    };
    this.token = jwt.sign(payload, this.clientSecret);
  }

  async request(method, path, data = null, headers = {}) {
    if (!this.token) {
      await this.authenticate();
    }

    const url = `${this.baseURL}${path}`;
    const options = {
      method,
      url,
      headers: {
        ...headers,
        Authorization: `Bearer ${this.token}`
      }
    };

    if (data) {
      options.data = data;
    }

    const response = await axios(options);
    return response.data;
  }
}

module.exports = APIClient;
