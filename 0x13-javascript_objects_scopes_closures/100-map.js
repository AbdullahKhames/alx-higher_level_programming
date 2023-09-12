#!/usr/bin/node
const ls = require('100-data.js').list;

const mapped = this.ls.map((x, index) => {
  return x * index;
});
console.log(ls);
console.log(mapped);
