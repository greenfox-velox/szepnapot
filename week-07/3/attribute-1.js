// Write the image's url to the console.
var images = document.querySelector('img');
console.log(images.getAttribute('src'));
// Replace the image with a picture of yourself.
images.setAttribute('src', 'https://tinyurl.com/z7lgzu5');

// Disable the second button.
var secondButton = document.querySelector('.this-one');
secondButton.disabled = true;
// Replace its text with 'Don't click me!'.
secondButton.textContent = 'Don\'t click me';
