#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const films = JSON.parse(body).results;
    const wedgeCount = films.filter(film =>
      film.characters.some(characterUrl => characterUrl.includes('/18/'))
    ).length;
    console.log(wedgeCount);
  }
});
