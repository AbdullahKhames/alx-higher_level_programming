#!/usr/bin/node
const x = Number.parseInt(process.argv[2]);

function fact (num) {
  if (isNaN(num)) {
    return 1;
  }
  if (num === 1) {
    return num;
  }
  return num * fact(num - 1);
}
console.log(fact(x));
