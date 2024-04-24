#!/usr/bin/node
const fs = require('fs');
const pathA = process.argv[2];
const pathB = process.argv[3];
const pathC = process.argv[4];

const contentsA = fs.readFileSync(pathA);
const contentsB = fs.readFileSync(pathB);
const contentsC = `${contentsA} \n ${contentsB}`;

fs.writeFileSync(pathC, contentsC);
