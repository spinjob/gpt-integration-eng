class Workflow {
  constructor(api1, api2) {
    this.api1 = api1;
    this.api2 = api2;
  }

  async step1() {
    const data = {
      testStoreId: process.env.TEST_STORE_ID
    };

    const headers = {
      'X-Store-Id': process.env.TEST_STORE_ID
    };

    const response = await this.api1.request('GET', '/getMenu', data, headers);
    return response;
  }

  async step2(menu) {
    const data = menu;
    const headers = {};

    const response = await this.api2.request('POST', '/upsertMenu', data, headers);
    return response;
  }

  async run() {
    const menu = await this.step1();
    const result = await this.step2(menu);
    return result;
  }
}

module.exports = Workflow;
