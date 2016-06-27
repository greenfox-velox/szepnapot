'use strict';

var numbers = [4, 5, 6, 7, 8, 9, 10]
// write your own sum function
function sumList(lista) {
  var sum = 0;
  for (var i = 0; i < lista.length; i++) {
    sum += lista[i];
  }
  return sum;
}

console.log(sumList(numbers));
