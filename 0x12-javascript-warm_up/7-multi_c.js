#!/usr/bin/node
const args = process.argv.slice(2);
if (args.length === 0 || isNaN(args[0])) {
  console.log('Missing number of occurrence');
} else {
  const x = parseInt(args[0]);
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
