// Import the express library
const express = require('express');

// Create an instance of an express application
const app = express();
// Define the port the server will listen on
const PORT = 7865;

// Define a route for the root URL (GET /)
app.get('/', (req, res) => {
  res.send('Welcome to the payment system');
});

// Only start the server if the file is run directly
if (require.main === module) {
  app.listen(PORT, () => {
    console.log(`API available on localhost port ${PORT}`);
  });
}

// Export the app for testing purposes
module.exports = app;
