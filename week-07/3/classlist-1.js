// Does cat have a cat class?
var allP = document.querySelectorAll('p');
if (document.querySelector('.cat')) { alert('YEAH CAT!'); };
// If so, alert 'YEAH CAT!'

// If dolphin has a 'dolphin' class, replace apple's content with 'pear'
if (document.querySelector('.dolphin')) { allP[0].textContent = 'pear'; }
// If apple has an 'apple' class, replace cat's content with 'dog'
if (document.querySelector('.apple')) { allP[2].textContent = 'dog'; }
// Make apple red
allP[0].classList += ' red';
// Make balloon less balloon-like
allP[1].classList = 'ballon-no-style';
