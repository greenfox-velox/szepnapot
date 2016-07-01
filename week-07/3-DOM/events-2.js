// On the click of the button,
// Count the items in the list
// And display the result in the result element.
var button = document.querySelector('button');

 function buttonClick () {
   var div = document.querySelectorAll('ul > li');
   var result = document.querySelector('.result');
   result.textContent = div.length;
 }
 button.addEventListener('click', buttonClick);
