// Remove the king from the list.

var asteroidList = document.querySelector('ul.asteroids');
var firstLi = document.querySelector('li');
asteroidList.removeChild(firstLi);

// Add list items that have the following text contents:
// ['apple', 'bubble', 'cat', 'green fox']

var listToAdd = ['apple', 'bubble', 'cat', 'green fox'];

function newLi (string){
  var newLi = document.createElement('li');
  newLi.textContent = string;
  return newLi;
}

for (var i = 0; i < listToAdd.length; i++) { asteroidList.appendChild(newLi(i, listToAdd[i])); }
