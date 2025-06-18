import { createClient , print} from "redis";
const client = createClient();
client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));
client.on('connect', () => console.log(`Redis client connected to the server`));

const obj = {
  Portland: '50',
  Seattle: '80',
  'New York': 20,
  Bogota: '20',
  Cali: '40',
  Paris: '2'
}

const keysArray = Object.keys(obj);
for (const key of keysArray) {
  client.hset('HolbertonSchools', key, obj[key], print);
}

client.hgetall('HolbertonSchools', function (err, res) {
  if (err) {
    console.log(err);
    throw new err;
  }
  console.log(res);
})
