// float2string(num) it should convert a float number to a string, for example 12.24 -> '12.24'

'use strict';

function float2string(number) {
  let stringOut = '';
  let startDivider = Math.log10(number);
  let decimalNotAdded = true;
  if (startDivider < 10) { startDivider = 1 };
  for ( var i = startDivider*10; i >= startDivider / 100; i /= 10 ) {
    if ( i < 1 && decimalNotAdded){
      stringOut += '.';
      decimalNotAdded = false;
    }
    var num = Math.floor(number / i);
    stringOut += num;
    number -= num * i;
  }
  return stringOut
}


console.log(float2string(12.24));
console.log(float2string(734.24));
console.log(float2string(2.4));
