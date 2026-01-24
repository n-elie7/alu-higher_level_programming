#!/usr/bin/node
const args = process.argv.slice(2);

const occurences = parseInt(args[0]);

if (args === undefined) {
    console.log('Missing number of occurrences');
}

for (let i = 0; i < occurences; i++) {
    console.log('C is fun');
}
