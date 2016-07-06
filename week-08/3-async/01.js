'use strict';

// create a function that takes a filename reads the content of the file
// and counts the words in it. It should not return the result, rather
// call a callback (its second parameter)
// The callback should have two parameters:
//  - err: the error object if anything wrong happened
//  - count: the word count

var fs = require('fs');

function wordCount(fileName, cb) {
  fs.readFile(fileName, 'utf8', function(err, content){
    if (err) { return cb(err); }
    let count = content.trim().split(/\s/).length;
    cb(err, count);
  })
}

wordCount('rando.txt', function(err, content) {
  console.log(err, content);
})
