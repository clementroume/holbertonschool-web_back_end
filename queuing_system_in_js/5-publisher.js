import { createClient } from 'redis';

// Create a new Redis client for publishing
const publisher = createClient();

// On successful connection
publisher.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Listen for the 'error' event to handle connection errors
publisher.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.toString()}`);
});

/**
 * Publishes a message to a Redis channel after a specified delay.
 * @param {string} message - The message to send.
 * @param {number} time - The delay in milliseconds before sending.
 */
const publishMessage = (message, time) => {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    publisher.publish('holberton school channel', message);
  }, time);
};

// Call the function with the required messages and delays
publishMessage('Holberton Student #1 starts course', 100);
publishMessage('Holberton Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300);
publishMessage('Holberton Student #3 starts course', 400);
