#!/usr/bin/node
const args = process.argv.slice(2);
let string = '';
if (args.length === 0) {
  string = 'undefined is undefined';
} else if (args.length === 1) {
  string = `${args[0]} is undefined`;
} else {
  string = `${args[0]} is ${args[1]}`;
}
console.log(string);
