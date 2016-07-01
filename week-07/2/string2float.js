// string2float(str) it should convert a string to a float number, for example '12.24' -> 12.24


'use strict';

function parseString(dict, str) {
  let num = 0;
  for (var i = 0; i <= str.length - 1; i++) {
    num += dict[str[i]] * (Math.pow(10, str.length - i - 1));
  }
  return num;
}

function string2float(str) {
  var numDict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9};
  var wholePart = str.split('.')[0];
  var complexPart = str.split('.')[1];
  var outFloat = 0;
  outFloat += parseString(numDict, wholePart);
  outFloat += parseString(numDict, complexPart) / Math.pow(10, complexPart.length);
  return outFloat;
}

console.log(string2float('12.24'));
