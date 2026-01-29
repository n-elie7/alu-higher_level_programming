#!/usr/bin/node

const Square = require('./5-square');

class SquareChar extends Square {
  charPrint (c) {
    const char = c === undefined ? 'X' : c;

    for (let i = 0; i < this.height; i++) {
      console.log(char.repeat(this.width));
    }
  }
}

const s1 = new SquareChar(4);
s1.charPrint();

s1.charPrint('C');

module.exports = SquareChar;
