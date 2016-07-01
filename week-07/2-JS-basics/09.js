'use strict';

// create a function that takes a string and counts its letters
// it should return an object thats keys are the letters and the values are
// the counts.
// example: "apple" -> {a: 1, p: 2, l: 1}

function countLetters (str) {
  var count = {};
  str.split('').forEach( function (c) { return count[c] ? count[c]++ : count[c] = 1});
  return count;
}

console.log(countLetters('apple'));
