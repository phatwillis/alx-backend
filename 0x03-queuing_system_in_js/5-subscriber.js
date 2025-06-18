import { createClient } from "redis";
const subsciber = createClient();
subsciber.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));
subsciber.on('connect', () => console.log(`Redis client connected to the server`));

const channel = 'holberton school channel'
subsciber.subscribe(channel);
subsciber.on('message', (channel, message) => {
  if (message === 'KILL_SERVER') {
    subsciber.unsubscribe(channel);
    subsciber.quit();
  }
  console.log(message);
})
