'use sttict';

var numbers = [7, 5, 8, -1, 2];
// Write a function that returns the minimal element
// in an array (your own min function)
function minOfList(lista) {
  min = 0;
  for (var i = 0; i < lista.length; i++) {
    if (lista[i] < min) {
      min = lista[i];
    }
  }
  return min;
}

console.log(minOfList(numbers));
