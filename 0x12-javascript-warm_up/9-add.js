#!/usr/bin/node
const num1 = Number.parseInt(process.argv[2]);
const num2 = Number.parseInt(process.argv[3]);
function add (a, b) {
  return a + b;
}
console.log(add(num1, num2));
