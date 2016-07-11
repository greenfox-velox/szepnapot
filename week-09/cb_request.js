'use strict';

function sendRequest(url, method, data, cb) {
  let xhr = new XMLHttpRequest();
  xhr.open(method, url);
  xhr.onload = function() {
    if ( xhr.readyState === 4) {
      let response = JSON.parse(xhr.responseText);
      cb(response)
    }
  }
  xhr.send(data && JSON.stringify(data));
}
