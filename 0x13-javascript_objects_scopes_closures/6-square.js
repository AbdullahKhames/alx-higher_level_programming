#!/usr/bin/node
const otherSquare = require('./5-square');

module.exports = class Square extends otherSquare {
  charPrint (ch) {
    if (ch === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let row = '';
        for (let j = 0; j < this.width; j++) {
          row += ch;
        }
        console.log(row);
      }
    }
  }
};
