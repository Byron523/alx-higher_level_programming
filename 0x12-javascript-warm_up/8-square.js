#!/usr/bin/node
// a script that prints a square

const n = Math.floor(Number(process.argv[2]));
if (isNaN(n)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      process.stdout.write('x');
    }
    console.log('');
  }
}
