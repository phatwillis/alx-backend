import { createClient } from "redis";
const client = createClient();
import { promisify } from "util";
client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));
client.on('connect', () => console.log(`Redis client connected to the server`));

const express = require('express');
const app = express();

const listProducts = [
  { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 }
];

const port = 1245;

function getItemById(id) {
  for (const product of listProducts) {
    if (product.id === id) {
      return product;
    }
  }
}

// set a stock amount in redis
// using the item id as key and the new stock as value
export function reserveStockById(itemId, stock) {
  client.set(itemId, stock);
}


// get current stock amount value
async function getCurrentReservedStockById(itemId) {
  const get = promisify(client.get).bind(client);
  const stock = await get(itemId).catch((error) => {
    console.log(error);
    throw error;
  });
  return stock;
}

app.get('/list_products', (req, res) => {
  res.send(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = req.params.itemId;
  const product = getItemById(parseInt(itemId));
  if (!product) {
    res.send({"status":"Product not found"});
  }
  const stockAmount = await getCurrentReservedStockById(parseInt(itemId));
  if (product) {
    if (stockAmount !== null) {
        const prettyProduct = {
        id: product.id,
        name: product.name,
        price: product.price,
        initialAvailableQuantity: product.stock,
        currentQuantity: parseInt(stockAmount)
        }
        res.send(prettyProduct);
    } else {
        const prettyProduct = {
        id: product.id,
        name: product.name,
        price: product.price,
        initialAvailableQuantity: product.stock,
        currentQuantity: product.stock
        }
        res.send(prettyProduct);
    }
  } 
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = req.params.itemId;
  const product = getItemById(parseInt(itemId));
  const stockAmount = await getCurrentReservedStockById(parseInt(itemId));

  if (!product) {
    res.json({"status":"Product not found"});
  }
  // if stock amount is null it is because that product has not been reserved.
  // if stock amount is null, subtract from the initial stock amount
  if (stockAmount === null) {
    reserveStockById(itemId, product.stock - 1);
    res.json({"status":"Reservation confirmed","itemId":itemId});
  } else {
      // else subtract from the redis stored stock amount
      if (parseInt(stockAmount) < 1) {
        // if it is less than 1 it means it is finished, cant reserve
        res.json({"status":"Not enough stock available","itemId":itemId});
      } else {
        reserveStockById(itemId, parseInt(stockAmount) - 1);
        res.json({"status":"Reservation confirmed","itemId":itemId});
      }
  }
})

app.listen(port);
export default app;
