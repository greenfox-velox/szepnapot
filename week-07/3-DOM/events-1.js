// Turn the party on and off by clicking the button.
var button = document.querySelector('button');

 function buttonOnOff (event) {
   var div = document.querySelector('div');
   div.classList.toggle('party');
 }
 button.addEventListener('click', buttonOnOff);
