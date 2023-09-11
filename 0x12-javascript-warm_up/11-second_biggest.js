#!/usr/bin/node
const arr = [];
let idx = 0;
let biggest = Number.MIN_SAFE_INTEGER;
let secondBiggest = Number.MIN_SAFE_INTEGER;
for (let i = 2; i < process.argv.length; i++, idx++) {
  arr[idx] = Number.parseInt(process.argv[i]);
}
if (arr.length === 0 || arr.length === 1) {
  console.log(0);
} else {
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > biggest) {
      secondBiggest = biggest;
      biggest = arr[i];
    } else if (arr[i] > secondBiggest) {
      secondBiggest = arr[i];
    }
  }
  console.log(secondBiggest);
}
