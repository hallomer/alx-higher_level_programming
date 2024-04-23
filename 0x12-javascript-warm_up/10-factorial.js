#!/usr/bin/node
const args = process.argv.slice(2);
function factorial (num) {
  if (isNaN(num) || num === 0) {
    return 1;
  }
  return num * factorial(num - 1);
}
let num;
if (args.length === 0) {
  num = 1;
} else {
  num = parseInt(args[0]);
}
console.log(factorial(num));
