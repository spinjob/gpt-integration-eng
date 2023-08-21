const axios = require('axios');

class API {
  constructor(baseUrl, token) {
    this.baseUrl = baseUrl;
    this.token = token;
  }

  async request(method, path, data, headers) {
    const url = `${this.baseUrl}${path}`;
    const options = {
      method,
      url,
      data,
      headers: {
        ...headers,
        Authorization: `Bearer ${this.token}`
      }
    };

    const response = await axios(options);
    return response.data;
  }
}

module.exports = API;
