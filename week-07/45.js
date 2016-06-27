'use strict';

var names = ['Zakarias', 'Hans', 'Otto', 'Ole'];
// create a function that returns the shortest string
// from an array


function shortestString(lista) {
  return lista.reduce(function (a, b) { return a.length < b.length ? a : b; });
}

console.log(shortestString(names));
