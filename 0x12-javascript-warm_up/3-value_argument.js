#!/usr/bin/node
const process = require('process');

const m = process.argv;
let x = 0;

m.forEach((val, index) => {
  x = x + 1;
});

if (x >= 2) {
  console.log(process.argv[2]);
} else if (x === 1) {
  console.log('No argument');
}
