class Workflow {
  constructor(getMenuRequest, upsertMenuRequest, dataMapper) {
    this.getMenuRequest = getMenuRequest;
    this.upsertMenuRequest = upsertMenuRequest;
    this.dataMapper = dataMapper;
  }

  async run() {
    const menu = await this.getMenuRequest.send('get');
    const mappedMenu = this.dataMapper.map(menu, mappingJson);
    await this.upsertMenuRequest.send('post', mappedMenu);
  }
}

module.exports = Workflow;
