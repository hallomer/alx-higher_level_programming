#!/usr/bin/node
const args = process.argv.slice(2);
function add (a, b) {
  console.log(a + b);
}
if (args.length === 0) {
  add();
} else if (args.length === 1) {
  add(parseInt(args[0]));
} else {
  add(parseInt(args[0]), parseInt(args[1]));
}
