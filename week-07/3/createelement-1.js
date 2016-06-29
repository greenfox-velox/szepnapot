// Add an item that says 'The Green Fox' to the asteroid list.
var asteroids = document.querySelector('ul.asteroids');
var newAsteroid = document.createElement('li');
newAsteroid.textContent = 'The Green Fox';
asteroids.appendChild(newAsteroid);
// Add an item that says 'The Lamplighter' to the asteroid list.
var newAsteroid1 = document.createElement('li');
newAsteroid1.textContent = 'The Lamplighter';
asteroids.appendChild(newAsteroid1);
// Add a heading saying 'I can add elements to the DOM!' to the .container.
var container = document.querySelector('.container');
container.textContent = 'I can add elements to the DOM!';
// Add an image, any image, to the container.
var newImg = document.createElement('img');
newImg.src = 'http://gallery.photo.net/photo/2495067-md.jpg';
container.appendChild(newImg);
