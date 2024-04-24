#!/usr/bin/node
const fs = require('fs');

const contentsA = fs.readFileSync(process.argv[2]);
const contentsB = fs.readFileSync(process.argv[3]);
const contentsC = contentsA + '\n' + contentsB + '\n';

fs.writeFileSync(process.argv[4], contentsC);
