#!/usr/bin/node
// script to get Wedge Antilles films
const request = require('request'); // Import the 'request' library

request
  .get(process.argv[2])
  .on('error', function (err) {
    console.error(err);
  })
  .on('response', function (response) {
    let responseData = '';
    let counter = 0;
    response.on('data', function (chunk) {
      responseData += chunk;
    });

    response.on('end', function () {
      try {
        const data = JSON.parse(responseData);
        const films = data.results;
        for (const film of films) {
          for (const character of film.characters) {
            if (character.indexOf('18') !== -1) {
              counter++;
            }
          }
        }
        console.log(counter);
      } catch (error) {
        console.error('Error parsing JSON:', error);
      }
    });
  });
