// // roman2int(number) it should convert a roman number as a string to an int, for example 'XII' -> 12
// please try to avoid using the built in conversion methods

function roman2int(roman) {
  var romanNumbers = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000 };
  var arabicInt = 0;
  var prevValue = 0;
  var i;
  for (i of roman) {
    if (romanNumbers[i] > prevValue) { arabicInt -= prevValue }
    else { arabicInt += prevValue }
    prevValue = romanNumbers[i];
  }
  arabicInt += prevValue;
  return arabicInt;
}

console.log(roman2int('DCXLIII'));
