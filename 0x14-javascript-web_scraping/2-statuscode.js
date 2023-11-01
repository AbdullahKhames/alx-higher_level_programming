#!/usr/bin/node
// get the code of a url
const request = require('request');
// request(process.argv[2], (error, response) => {
//   if (error) {
//     console.error(error);
//   } else {
//     console.log('code: ', response.statusCode);
//   }
// });
request
  .get(process.argv[2])
  .on('error', function (err) {
    console.error(err);
  })
  .on('response', function (response) {
    console.log('code: ' + response.statusCode);
  });
