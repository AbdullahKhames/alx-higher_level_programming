#!/usr/bin/node
// get the code of a url
const request = require('request');
request(process.argv[2], (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('code: ', response.statusCode);
  }
});
