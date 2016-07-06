
'use strict';

// create a function that has 2 paramteres
//  - fileNames: an array of filenames
//  - callback
//
// it should read the files and call the callback with their content concated
// it should have the same order as the filenames
// it should pass the error as a parameter
var fs = require('fs');
var files = ['test.txt', 'test1.txt', 'random.txt'];


function fileConcater(file, cb) {
  fs.readFile(file, 'utf8', function(err, content) {
    if (err) {return cb(err);}
    let contentFromFile = content.trim();
    cb(null, contentFromFile);
  })
}

for (var i = 0; i < files.length; i++) {
  var concated = '';
  var passed = 0;
  fileConcater(files[i], function(err, cont) {
    concated += cont;
    passed += 1;
    if (passed === 3) {console.log(concated);}
  })
}
