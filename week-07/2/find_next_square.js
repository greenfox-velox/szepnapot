'use strict';

var isSquare = function (n) {
    return n > 0 && Math.sqrt(n) % 1 === 0;
}

function findNextSquare(sq) {
  if (isSquare(sq)){
    var nextPerfect = 0;
    for ( var i = sq + 1; nextPerfect > 0; i++ ){
      if (isSquare(i)) {
        nextPerfect = i;
        return nextPerfect;
      }
      }
    } else {
  return -1;
}
}
console.log(findNextSquare(121));
console.log(isSquare(121));
