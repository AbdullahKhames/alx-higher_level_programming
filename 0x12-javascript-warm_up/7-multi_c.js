#!/usr/bin/node
const maxOccurence = Number.parseInt(process.argv[2]);
if (isNaN(maxOccurence)) {
  console.log('Missing number of occurrences');
}
let i = 0;
while (i < maxOccurence) {
  console.log('C is fun');
  i++;
}
