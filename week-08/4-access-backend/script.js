var xhr = new XMLHttpRequest();
var submitButton = document.querySelector('#yoda');
var translated = document.querySelector('p');

var getRequestBody = function(event) {
  event.preventDefault();
  let sentence = document.querySelector('#sentence').value;
  sentence.replace(' ','+');
  var complete = '?sentence=' + sentence;
  xhr.open("GET", 'https://yoda.p.mashape.com/yoda' + complete, true);

  xhr.setRequestHeader("X-Mashape-Key", "ixPdA6QnDImshS3hdqwfveb6RXkGp10gUisjsnZh5e93gcviIE",
                        "Accept", "text/plain")

  xhr.send(null);
  xhr.onload = function() {
    translated.textContent = xhr.responseText;
  }
};
submitButton.addEventListener("click", getRequestBody);
