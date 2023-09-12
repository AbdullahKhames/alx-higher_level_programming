#!/usr/bin/node
const converter = require('./10-converter.js').converter;

let myConv = converter(10);
myConv(15);
myConv = converter(16);
myConv(15);
