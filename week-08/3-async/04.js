'use strict';

// Create a function that takes 3 parameters
//  - file1: a filename
//  - file2: a filename
//  - cb: callback (with two paramteres: error and contents)
//
// It should read both files and concat their content
// then it should call the callback with the concated contents
// if any error occures it should call the callback with an error

var fs = require('fs');

function concatTwoFiles(file1, file2, cb) {
  fs.readFile(file1, 'utf8', function(err, content){
    if (err) { return cb(err);}
    var contFromFiles = content.replace('\n', ' ');
    fs.readFile(file2, 'utf8', function(err, content){
      if (err) { return cb(err);}
      contFromFiles += content.replace('\n', ' ');
      cb(null, contFromFiles);
    })
  })
}

concatTwoFiles('test.txt', 'test1.txt', function(err, cont){
  console.log(err, cont);
})
