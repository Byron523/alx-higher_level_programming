#!/usr/bin/node
// a script that add twi ints

const a = process.argv.length;
if (a === 4) {
  console.log(add(Number(process.argv[2]), Number(process.argv[3])));
} else {
  console.log('NaN');
  process.exit(1);
}

function add (a, b) {
  return a + b;
}
