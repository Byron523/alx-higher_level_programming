#!/usr/bin/node

const myNumber = process.argv[2];

const mine = Number(myNumber);
if (Number.isInteger(mine)) {
  console.log(`My number: ${mine}`);
} else {
  console.log('Not a number');
}
