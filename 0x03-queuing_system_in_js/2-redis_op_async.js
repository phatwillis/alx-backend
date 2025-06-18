import { createClient, print} from "redis";
import { promisify } from 'util';
const client = createClient();
client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));
client.on('connect', () => console.log(`Redis client connected to the server`));

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

async function displaySchoolValue(schoolName) {
  const get = promisify(client.get).bind(client);
  const schoolValue = await get(schoolName).catch((error) => {
    console.log(error);
    throw error;
  });
  console.log(schoolValue);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
