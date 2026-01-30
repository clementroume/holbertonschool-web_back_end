import { createClient, print } from 'redis';

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

// The data to be stored in the hash
const hashValues = {
  Portland: '50',
  Seattle: '80',
  'New York': '20',
  Bogota: '20',
  Cali: '40',
  Paris: '2',
};

// Use hset to store each field-value pair in the 'HolbertonSchools' hash
for (const [field, value] of Object.entries(hashValues)) {
  client.hset('HolbertonSchools', field, value, print);
}

// Use hgetall to retrieve the entire hash and display it
client.hgetall('HolbertonSchools', (err, reply) => {
  if (err) {
    console.error(err);
  } else {
    console.log(reply);
  }
});
