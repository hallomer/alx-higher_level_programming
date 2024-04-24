#!/usr/bin/node
let count = 0;
exports.logMe = function (item) {
  const i = `${count}: ${item}`;
  console.log(i);
  count += 1;
};
