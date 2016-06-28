'use strict';

var numbers = [2, 5, 11, 29];

// create a function that takes an array of numbers and returns a boolean
// it should return true if all the elements are prime, false otherwise

function isPrime(value) {
  for (var i = 2; i < value/2; i++) {
    if(value % i === 0) {
      return false;
    }
  }
  return value > 1;
}
function isPrimeList(arr) {
  return arr.every(isPrime)
}

console.log(isPrimeList(numbers));
