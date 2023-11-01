#!/usr/bin/node
const request = require('request');
const options = {
  method: 'GET',
  uri: `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`
};
request(options, (error, response, data) => {
  if (!error) {
    const characters = JSON.parse(data).characters;
    prictActors(characters, 0);
  }
});

function prictActors (characters, index) {
  request(characters[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        prictActors(characters, index + 1);
      }
    }
  });
}
