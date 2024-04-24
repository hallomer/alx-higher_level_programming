#!/usr/bin/node
const { dict } = require('./101-data.js');
const newDict = {};
for (const [id, occurrences] of Object.entries(dict)) {
  if (!newDict[occurrences]) {
    newDict[occurrences] = [];
  }
  newDict[occurrences].push(id.toString());
}

console.log(newDict);
