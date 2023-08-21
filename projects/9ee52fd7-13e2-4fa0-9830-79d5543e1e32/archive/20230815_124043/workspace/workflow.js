class Workflow {
  constructor(apiClient) {
    this.apiClient = apiClient;
  }

  async executeStep1(dataMapping) {
    const { input, output } = dataMapping['X-Store-Id'];
    const data = { [input.key]: input.value };
    const headers = { [output.key]: output.value };
    const response = await this.apiClient.request('GET', '/getMenu', data, headers);
    return response;
  }

  async executeStep2(dataMapping, previousResponse) {
    const data = {};
    const headers = {};

    for (const key in dataMapping) {
      const { input, output } = dataMapping[key];
      const value = previousResponse[input.path];
      if (output.in === 'body') {
        data[output.path] = value;
      } else if (output.in === 'header') {
        headers[output.path] = value;
      }
    }

    const response = await this.apiClient.request('POST', '/upsertMenu', data, headers);
    return response;
  }
}

module.exports = Workflow;
