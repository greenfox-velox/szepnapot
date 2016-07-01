// fill output1 with the first paragraph's content, text only.
var paragraphs = document.querySelectorAll('p');
// fill output2 with the first paragraph's content keeping the cat strong.
paragraphs[1].textContent = paragraphs[0].textContent;
paragraphs[2].innerHTML = paragraphs[0].innerHTML;
