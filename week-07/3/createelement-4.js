// Remove the king from the list.
'use strict';
var asteroidList = document.querySelector('ul.asteroids');
var firstLi = document.querySelector('li');
asteroidList.removeChild(firstLi);

// Fill the list based on the following list of objects:
var planetData = [
  {
    category: 'inhabited',
    content: 'Foxes',
    asteroid: true
  },
  {
    category: 'inhabited',
    content: 'Whales and Rabbits',
    asteroid: true
  },
  {
    category: 'uninhabited',
    content: 'Baobabs and Roses',
    asteroid: true
  },
  {
    category: 'inhabited',
    content: 'Giant monsters',
    asteroid: false
  },
  {
    category: 'inhabited',
    content: 'Sheep',
    asteroid: true
  }
]
// only add the asteroids to the list.
// each list item should have its category as a class
// and its content as text content.

function newLi (id, className, content){
  var newLi = document.createElement('li');
  newLi.id = id;
  newLi.textContent = content;
  newLi.classList.add(className);
  return newLi;
}
for (var i = 0; i < planetData.length; i++) {
  var currentObj = planetData[i];
  console.log(currentObj);
  if (currentObj['asteroid']) { asteroidList.appendChild(newLi(i, currentObj['category'], currentObj['content'])) }

}
