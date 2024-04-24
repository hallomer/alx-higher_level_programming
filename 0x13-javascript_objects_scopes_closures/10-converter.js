#!/usr/bin/node
exports.converter = function (base) {
  function toBase (num) {
    return num.toString(base);
  }
  return toBase;
};
