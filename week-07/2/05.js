
'use strict';

var numbers = [2.4, 3.5, 1.7, 3.3, 1.2];

// create a function that takes an array of numbers,
// it should return a new array that consists only the numbers that are
// bigger than 2 and all of it's elements should be rounded

function checkNum(n) { return n > 2; }
function roundNum(n) { return Math.round(n); }
function createList(arr) { var goodNums = arr.filter(checkNum); return goodNums.map(roundNum); };
console.log(createList(numbers));
