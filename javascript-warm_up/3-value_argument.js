#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length === 0) {
  console.log('No argument');
} else {
    for (let i = 0; i < args.length; i++) {
        console.log(args[i]);
    }
}
