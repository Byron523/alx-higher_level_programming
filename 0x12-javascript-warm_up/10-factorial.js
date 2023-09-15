#!/usr/bin/node
// a script taht prints a factorial

function fact (m) {
  return m === 0 || isNaN(m) ? 1 : m * fact(m - 1);
}

console.log(fact(Number(process.argv[2])));
