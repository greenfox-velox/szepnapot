// fill every paragraph with the last one's content.
var paragraphs = document.querySelectorAll('p');
var contentToFill = paragraphs[paragraphs.length - 1].textContent;
for (var i = 0; i < paragraphs.length; i++) {
  paragraphs[i].textContent = contentToFill;
}
console.log(paragraphs);
