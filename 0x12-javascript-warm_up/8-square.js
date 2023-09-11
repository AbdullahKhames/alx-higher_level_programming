#!/usr/bin/node
const size = Number.parseInt(process.argv[2]);
if (isNaN(size)) {
  console.log('Missing size');
}
let i = 0;
while (i < size) {
  let row = '';
  for (let j = 0; j < size; j++) {
    row += 'X';
  }
  console.log(row);
  i++;
}
