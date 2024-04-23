#!/usr/bin/node
const args = process.argv.slice(2);
const numbers = args.map(Number);

function secondBig (args) {
  let first = -Infinity;
  let second = -Infinity;
  for (const arg of args) {
    if (arg > first) {
      second = first;
      first = arg;
    } else if (arg > second && arg !== first) {
      second = arg;
    }
  }
  return second;
}
if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  console.log(secondBig(numbers));
}
