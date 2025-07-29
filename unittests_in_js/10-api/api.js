// Import the express library
const express = require('express');

// Create an instance of an express application
const app = express();
// Define the port the server will listen on
const PORT = 7865;

// Middleware to parse JSON bodies
app.use(express.json());

// Define a route for the root URL (GET /)
app.get('/', (req, res) => {
  res.send('Welcome to the payment system');
});

// Define a route for the root URL (GET /)
app.get('/cart/:id(\\d+)', (req, res) => {
  const { id } = req.params;
  res.send(`Payment methods for cart ${id}`);
});

// Define a route for available payment methods
app.get('/available_payments', (req, res) => {
  res.json({
    payment_methods: {
      credit_cards: true,
      paypal: false,
    },
  });
});

// Define a route for user login
app.post('/login', (req, res) => {
  const { userName } = req.body;
  if (userName) {
    res.send(`Welcome ${userName}`);
  } else {
    res.status(400).send('Bad Request');
  }
});

// Only start the server if the file is run directly
if (require.main === module) {
  app.listen(PORT, () => {
    console.log(`API available on localhost port ${PORT}`);
  });
}

// Export the app for testing purposes
module.exports = app;
