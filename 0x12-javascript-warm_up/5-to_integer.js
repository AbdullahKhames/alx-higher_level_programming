#!/usr/bin/node
const x = Number.parseInt(process.argv[2]);
if (isNaN(x)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + x);
}
