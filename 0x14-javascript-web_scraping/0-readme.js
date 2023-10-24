#!/usr/bin/node
// script to read and input a command line file
const fs = require('fs');
const arguments = process.argv;
const filePath = arguments[2];
fs.readFile(filePath, 'utf8', (err, data) =>{
    if (err){
        console.log(err);
        return;
    }
    else {
        console.log(data);
    }
});
