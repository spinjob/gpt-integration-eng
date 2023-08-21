require('dotenv').config();
const express = require('express');
const APIClient = require('./apiClient');
const Workflow = require('./workflow');

const app = express();
app.use(express.json());

const apiClient = new APIClient(
  process.env.API_BASE_URL,
  process.env.API_CLIENT_ID,
  process.env.API_CLIENT_SECRET
);

const workflow = new Workflow(apiClient);

app.post('/trigger', async (req, res) => {
  try {
    const step1DataMapping = req.body.step1DataMapping;
    const step1Response = await workflow.executeStep1(step1DataMapping);

    const step2DataMapping = req.body.step2DataMapping;
    const step2Response = await workflow.executeStep2(step2DataMapping, step1Response);

    res.json(step2Response);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

const port = process.env.PORT || 3000;
app.listen(port, () => console.log(`Server listening on port ${port}`));
