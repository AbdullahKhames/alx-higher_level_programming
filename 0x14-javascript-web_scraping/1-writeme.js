#!/usr/bin/node
// script to write to a file given as args
const fileSys = require('fs');
const fileName = process.argv[2];
const toWrite = process.argv[3];
fileSys.writeFile(fileName, toWrite, 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
