#!/usr/bin/node
exports.converter = function (base) {
  if (base === 10) {
    return function (num) {
      console.log(num);
    };
  } else if (base === 16) {
    return function (num) {
      console.log(num.toString(16));
    };
  } else if (base === 2) {
    return function (num) {
      console.log(num.toString(2));
    };
  }
};
