#!/usr/bin/node
const process = require('process');

const m = process.argv;
let x = 0;

m.forEach((val, index) => {
  x = x + 1;
});

if (x === 2) {
  console.log('No argument');
} else if (x === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
