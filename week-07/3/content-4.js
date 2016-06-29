// replace the list items' content with items from this list:
// ['apple', 'banana', 'cat', 'dog']
var replaceWords = ['apple', 'banana', 'cat', 'dog'];
var list = document.querySelectorAll('ul > li');
for (var i = 0; i < list.length; i++) {
  list[i].textContent = replaceWords[i];
}
