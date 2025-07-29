import { createClient, print } from 'redis';
import { promisify } from 'util';

// Create a new Redis client
const client = createClient();

// Listen for the 'connect' event to confirm a successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Listen for the 'error' event to handle connection errors
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.toString()}`);
});

/**
 * Sets a new value for a given key in Redis.
 * @param {string} schoolName - The key to set.
 * @param {string} value - The value to set for the key.
 */
const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, print);
};

// Promisify the client.get method to use it with async/await
const getAsync = promisify(client.get).bind(client);

/**
 * Displays the value of a given key from Redis.
 * @param {string} schoolName - The key to retrieve.
 */
async function displaySchoolValue(schoolName) {
  try {
    const reply = await getAsync(schoolName);
    console.log(reply);
  } catch (err) {
    console.error(err);
  }
}

// Call the functions as required
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
