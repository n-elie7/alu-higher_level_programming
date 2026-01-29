#!/usr/bin/node

let count = 0;

exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count++;
};

const logMe = require('./9-logme').logMe;
