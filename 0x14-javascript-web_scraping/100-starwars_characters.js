#!/usr/bin/node
const request = require('request');
options = {
  method: 'GET',
  uri: `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`
};
request(options, (error, response, data) => {
  if (error) {
    console.error(error);
  }
  actors = JSON.parse(data).characters;
  for (actorUrl of actors) {
    options = {
      method: 'GET',
      uri: `${actorUrl}`
    };
    request(options, (error, response, data) => {
      if (error) {
        console.error(error);
      }
      actor = JSON.parse(data);
      console.log(actor.name);
    })
  }
});
