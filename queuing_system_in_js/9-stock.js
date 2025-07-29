import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';

// --- Data ---
const listProducts = [
  {
    itemId: 1,
    itemName: 'Suitcase 250',
    price: 50,
    initialAvailableQuantity: 4,
  },
  {
    itemId: 2,
    itemName: 'Suitcase 450',
    price: 100,
    initialAvailableQuantity: 10,
  },
  {
    itemId: 3,
    itemName: 'Suitcase 650',
    price: 350,
    initialAvailableQuantity: 2,
  },
  {
    itemId: 4,
    itemName: 'Suitcase 1050',
    price: 550,
    initialAvailableQuantity: 5,
  },
];

// --- Data Access ---
function getItemById(id) {
  return listProducts.find((item) => item.itemId === id);
}

// --- Redis Client Setup ---
const client = createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.toString()}`);
});

client.on('connect', () => {
  // console.log('Redis client connected to the server');
});

// --- Stock Functions ---
async function reserveStockById(itemId, stock) {
  await setAsync(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
  const stock = await getAsync(`item.${itemId}`);
  return stock;
}

// --- Express Server Setup ---
const app = express();
const port = 1245;

// --- Routes ---

// Route to get the list of all products
app.get('/list_products', (req, res) => {
  res.json(
    listProducts.map((item) => ({
      itemId: item.itemId,
      itemName: item.itemName,
      price: item.price,
      initialAvailableQuantity: item.initialAvailableQuantity,
    }))
  );
});

// Route to get a specific product's details and stock
app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const item = getItemById(itemId);

  if (!item) {
    return res.json({ status: 'Product not found' });
  }

  const currentStock = await getCurrentReservedStockById(itemId);
  const availableStock =
    currentStock === null
      ? item.initialAvailableQuantity
      : parseInt(currentStock, 10);

  res.json({
    ...item,
    currentQuantity: availableStock,
  });
});

// Route to reserve a product
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const item = getItemById(itemId);

  if (!item) {
    return res.json({ status: 'Product not found' });
  }

  const currentStockStr = await getCurrentReservedStockById(itemId);
  const currentStock =
    currentStockStr === null
      ? item.initialAvailableQuantity
      : parseInt(currentStockStr, 10);

  if (currentStock < 1) {
    return res.json({
      status: 'Not enough stock available',
      itemId: item.itemId,
    });
  }

  await reserveStockById(itemId, currentStock - 1);
  res.json({ status: 'Reservation confirmed', itemId: item.itemId });
});

// --- Start Server ---
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
