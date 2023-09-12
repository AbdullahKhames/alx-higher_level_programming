#!/usr/bin/node
const dict = require('./101-data.js').dict;
const newDic = {};
for (const prop in dict) {
  if (!newDic[dict[prop]]) {
    newDic[dict[prop]] = [];
  }
  newDic[dict[prop]].push(prop);
}
console.log(newDic);
