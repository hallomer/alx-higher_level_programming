#!/usr/bin/node
const { list } = require('./100-data.js');
const newArr = list.map((value, index) => value * index);

console.log(list);
console.log(newArr);
