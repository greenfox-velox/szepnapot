// Remove the king from the list.
var asteroidList = document.querySelector('ul.asteroids');
var firstLi = document.querySelector('li');
asteroidList.removeChild(firstLi);
// Add 3 list items saying 'The Fox' to the list.
function newLi (id){
  var newLi = document.createElement('li');
  newLi.id = id;
  newLi.textContent = 'The Fox';
  return newLi;
}
for (var i = 0; i < 3 ; i++) { asteroidList.appendChild(newLi(i)); }
