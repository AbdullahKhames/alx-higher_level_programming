#!/usr/bin/node
// hitting starwars api
const request = require('request');
movieID = process.argv[2];
fullUrl = `https://swapi-api.alx-tools.com/api/films/${movieID}`
request(fullUrl, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(response.body);
    console.log(data.title);
  }
})
