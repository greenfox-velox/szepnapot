'use strict';

// Create a function that takes a number and returns it as string in english
// like 0 -> "zero", it should work with the first 5 numbers, after it should
// return "many"

var numbersDict = {0 : 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'};

function englishNumbers(n) {return numbersDict[n] || 'many'};

console.log(englishNumbers(6));
