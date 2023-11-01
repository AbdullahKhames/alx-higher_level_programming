#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file

const request = require('request');
const fileSys = require('fs');
const options = {
  method: 'GET',
  uri: `${process.argv[2]}`
};
request(options, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    fileSys.appendFile(process.argv[3], body, 'utf-8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
