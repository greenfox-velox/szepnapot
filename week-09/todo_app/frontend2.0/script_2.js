'use strict';
var host = 'http://jsonplaceholder.typicode.com';

function sendRequest(method, url, data, cb) {
  var xhr = new XMLHttpRequest();
  xhr.open(method, host + url);
  xhr.setRequestHeader("content-type",'application/json');
  xhr.setRequestHeader('Access-Control-Allow-Origin', '*');
  xhr.onload = function() {
    if ( xhr.readyState === 4) {
      cb(null, JSON.parse(xhr.responseText))
    }
  }
  xhr.send(data && JSON.stringify(data));
}

// module.exports.ajax = sendRequest;

sendRequest('GET', '/posts/1', '', function(err, cont){
  if (err) {
    console.log(err);
  }
  console.log(cont);
})

// exports.sendRequest = sendRequest;
