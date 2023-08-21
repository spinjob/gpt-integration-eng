require('dotenv').config();
const API = require('./api');
const Workflow = require('./workflow');

const api1 = new API(process.env.API_1_BASE_URL, process.env.API_1_TOKEN);
const api2 = new API(process.env.API_2_BASE_URL, process.env.API_2_TOKEN);

const workflow = new Workflow(api1, api2);

workflow.run()
  .then(result => console.log(result))
  .catch(error => console.error(error));
