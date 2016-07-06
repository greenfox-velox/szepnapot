'use strict';

// create a function takes three parameters:
//  - fileName: the name of the file
//  - letter: a character
//  - cb: callback (with two parameters: error and the result)
//
// it should read the file and count the letters in the content
// and it should call the callback with the counted number
// if there is some error it should call the callback with the error
//

var fs = require('fs');

function characterCounter(fileName, letter, cb) {
  fs.readFile(fileName, 'utf8', function(err, content){
    if (err) { return cb(err); }
    let re = new RegExp(letter, 'g');
    var totalLetters = content.match(re).length;
    cb(err, totalLetters);
  })
}

characterCounter('random.txt', 'é', function(err, content){
  console.log(err, content);
})
