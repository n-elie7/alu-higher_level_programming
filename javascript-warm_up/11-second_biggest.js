#!/usr/bin/node

const args = process.argv.slice(2);

const sortedArray = args.sort((a, b) => b - a);

console.log(sortedArray[1]);
