
'use strict';

// create a function that takes 3 parameters
//  - readFileName: a filename where it reads from
//  - wirteFileName: a filename where it writes to
//  - cb: callback with one parameter: the error if occured
//
// It should read the file named readFileName and double the text of the file
// like: "apple" -> "appleapple"
// Than it should write this doubled text to the file named writeFileName
// When it finished it should call the callback with a null
// If there is any error during the process it should call the callback with the error

var fs = require('fs');

function loadAndWrite(readFileName, writeFileName, cb) {
  fs.readFile(readFileName, 'utf8', function(err, content){
    if (err) { return cb(err); }
    let trimmedContent = content.trim();
    let writeOut = trimmedContent + trimmedContent;
    fs.writeFile(writeFileName, writeOut, 'utf8', function(err, content){
      if (err) { return cb(err);}
      return cb(null);
    })
  })
}

loadAndWrite('test.txt', 'copy.txt', function(err, cont){
  console.log(err);
})
