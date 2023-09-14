#!/usr/bin/node
// printing c is fun a number of times

const n = process.argv.length - 2;
if (n < 2) {
  console.error('Missing number of occurences');
}

const m = Number(process.argv[2]);

if (Number.isInteger(m)) {
  for (let i = 0; i < m; i++) {
    console.log('C is fun');
  }
}
