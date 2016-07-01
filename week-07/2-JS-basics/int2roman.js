// int2roman(number) it should convert an int number to a roman number as a string, for example 12 -> 'XII'

var romanNumbers = { 'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50,
                      'XL': 40, 'X': 10, 'IX': 9, 'V':5, 'IV': 4, 'I': 1}
function int2roman(number) {
  var romanInt = '';
  var i;
  for (i in romanNumbers) {
    while ( number >= romanNumbers[i]) {
      romanInt += i;
      number -= romanNumbers[i];
    }
  }
  return romanInt;
}

// function converter() {
//   var num2Convert = parseInt(prompt("Enter ARABIC number: "));
//   num2Convert > 4000 ? alert("Number too big. Must below 4000.") : int2roman(num2Convert);
// }


console.log(int2roman(1234));
