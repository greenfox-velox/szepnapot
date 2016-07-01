// 1. Alert the content of the header.
var headContent = document.querySelector('head');
alert(headContent.textContent);
// 2. Write the content of the first paragraph to the console.
var firstP = document.querySelector('p');
console.log(firstP.textContent);
// 3. Alert the content of the second paragraph.
var ps = document.querySelectorAll('p')
alert(ps[1].textContent)
// 4. Replace the heading's content with 'New content'.
headContent.textContent = 'New Content';
console.log(headContent.textContent);
// 5. Replace the last paragraph's content with the first paragraph's content.
ps[2].textContent = ps[0].textContent;
console.log(ps[2]);
