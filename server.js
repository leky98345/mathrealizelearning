const express = require('express');
const axios = require('axios');
const app = express();
const port = 3000;

app.use(express.static('public'));
app.use(express.urlencoded({ extended: true }));

// Endpoint to handle proxy requests
app.post('/fetch-url', async (req, res) => {
  const url = req.body.url;

  try {
    const response = await axios.get(url, {
      proxy: {
        host: '198.23.239.134',
        port: 6540,
        auth: {
          username: 'ibbcndrl',
          password: 'c3pldcx962xr'
        }
      },
      timeout: 10000 // Timeout increased for large responses
    });

    res.send(response.data); // Send proxied data back to the client
  } catch (error) {
    console.error('Error:', error.message);

    // Custom error responses for different scenarios
    if (error.response) {
      res.status(error.response.status).send(`Error: Received ${error.response.status} from the target server.`);
    } else if (error.code === 'ECONNABORTED') {
      res.status(504).send('Error: Request timed out.');
    } else if (error.message.includes('proxy')) {
      res.status(502).send('Error: Proxy server unreachable or credentials incorrect.');
    } else {
      res.status(500).send('Error: Unable to fetch the URL.');
    }
  }
});

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});
