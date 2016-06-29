// 1. store the element that says 'The King' in the 'king' variable.
// console.log it.
'use strict';

var king = document.querySelector('.asteroid');
console.log(king);

// 2. store the element that contains the text 'The Conceited Man'
// in the 'conceited' variable.
// show the result in an 'alert' window.
var conceited = document.querySelector('.b326');
alert(conceited);


// 3. store 'The Businessman' and 'The Lamplighter'
// in the 'businessLamp' variable.
// console.log each of them.
var businessLamp = document.querySelectorAll('.big');
console.log(businessLamp[0]);
console.log(businessLamp[1]);

// 4. store 'The King' and 'The Conceited Man'
// in the 'conceitedKing' variable.
// alert them one by one.
var conceitedKing = document.querySelectorAll('.container > .asteroid');
console.log(conceitedKing);
var print = conceitedKing.forEach(alert);
print;


// 5. store 'The King', 'The Conceited Man' and 'The Lamplighter'
// in the 'noBusiness' variable.
// console.log each of them.
var noBusiness = document.querySelectorAll('div.asteroid');
for (var i = 0; i < noBusiness.length; i++) {
  console.log(noBusiness[i]);
}

// 6. store 'The Businessman' in the 'allBizniss' variable.
// show the result in an 'alert' window.
var allBizniss = document.querySelector('p');
alert(allBizniss);
