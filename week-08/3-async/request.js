var button = document.querySelector('#request');
button.addEventListener('click', getWorkDay);
var currentWorkDay = document.querySelector('p');
var xhr = new XMLHttpRequest();
function getWorkDay(){
  preloader();
  let xhr = new XMLHttpRequest();
  xhr.open('GET','http://calapi.inadiutorium.cz/api/v0/en/calendars/default/today', true)
  xhr.responseType = 'json';
  xhr.onload = function () {
    if (xhr.readyState === xhr.DONE) {
      if (xhr.status === 200) {
        loaded();
        let celebrations = xhr.response.celebrations.length;
        let currentDay = xhr.response.weekday;
        let htmlCeleb = document.createElement('h1');
        htmlCeleb.textContent = "There are " + celebrations + " celebrations today.";
        let htmlDay = document.createElement('h1');
        htmlDay.textContent = "It's " + currentDay;
        currentWorkDay.appendChild(htmlDay);
        currentWorkDay.appendChild(htmlCeleb);
      }
  }
};
  xhr.send(null);
}

function preloader() {
  document.querySelector('.loading').style.display = "block";
  document.querySelector('button').style.display = "none";
}
function loaded() {
  document.querySelector('.loading').style.display = "none";
  document.querySelector('button').style.display = "inline-block";
}
