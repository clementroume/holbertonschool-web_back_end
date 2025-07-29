import { createClient } from 'redis';

// Create a new Redis client for subscribing
const subscriber = createClient();
const channel = 'holberton school channel';

// On successful connection
subscriber.on('connect', () => {
  console.log('Redis client connected to the server');
  // Subscribe to the specified channel
  subscriber.subscribe(channel);
});

// Listen for the 'error' event to handle connection errors
subscriber.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.toString()}`);
});

subscriber.on('message', (receivedChannel, message) => {
  console.log(message);
  // If the message is KILL_SERVER, unsubscribe and quit
  if (message === 'KILL_SERVER') {
    subscriber.unsubscribe(channel);
    subscriber.quit();
  }
});
