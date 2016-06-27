'use strict';

// create a function that returns it's input factorial

function range(start, end) {
  var foo = [];
  for (var i = start; i <= end; i++) {
    foo.push(i);
  }
return foo;
}

function nthFactorial(userNumber) {
  console.log(range(1, userNumber).reduce((a, b) => a * b, 1));
}
nthFactorial(5);
