const express = require('express');
const axios = require('axios');
const app = express();
const port = process.env.PORT || 3000;

app.use(express.static('public'));
app.use(express.urlencoded({ extended: true }));

// Endpoint to handle proxy requests
app.post('/fetch-url', async (req, res) => {
  // Testing with a fixed URL to see if the proxy connection works
  const testUrl = 'https://jsonplaceholder.typicode.com/todos/1';
  
  console.log(`Attempting to access URL: ${testUrl} through the proxy`);

  try {
    const response = await axios.get(testUrl, {
      proxy: {
        host: '198.23.239.134',
        port: 6540,
        auth: {
          username: 'ibbcndrl',
          password: 'c3pldcx962xr'
        }
      },
      timeout: 5000 // Timeout set to 5 seconds
    });
    
    res.send(response.data); // Display the proxied page content
  } catch (error) {
    console.error('Error details:', error.message);

    // Show the error message on the web page for easier troubleshooting
    if (error.response) {
      res.send(`Error: Received ${error.response.status} from the server.`);
    } else if (error.code === 'ECONNABORTED') {
      res.send('Error: Request timed out. The server might be unresponsive.');
    } else if (error.message.includes('proxy')) {
      res.send('Error: Proxy server unreachable or credentials incorrect.');
    } else {
      res.send('Error: Unable to fetch the URL. Check if the proxy or URL is correct.');
    }
  }
});

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});
