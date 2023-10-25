#!/usr/bin/node
// script to read file
const fileSys = require('fs');
const fileName = process.argv[2];
fileSys.readFile(fileName, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
