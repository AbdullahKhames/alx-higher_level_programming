#!/usr/bin/node
const request = require('request');
const options = {
  method: 'GET',
  uri: `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`
};
request(options, (error, response, data) => {
  if (error) {
    console.error(error);
  }
  const actors = JSON.parse(data).characters;
  for (const actorUrl of actors) {
    const options = {
      method: 'GET',
      uri: `${actorUrl}`
    };
    request(options, (error, response, data) => {
      if (error) {
        console.error(error);
      }
      const actor = JSON.parse(data);
      console.log(actor.name);
    });
  }
});
