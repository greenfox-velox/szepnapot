'use strict';

var numbers = [3, 4, 5, 6, 7];
// write a function that filters the odd numbers
// from an array and returns a new array consisting
// only the evens

function is_odd(number) {
  return number % 2 !== 0;
}

function oddFilter(lista) {
  var oddList = lista.filter(is_odd);
  return oddList;
}

console.log(oddFilter(numbers));
