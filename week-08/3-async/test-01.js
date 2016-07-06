var countStringInFile = require('./01');
var countLetters = countStringInFile.countString;
var countLettersInFile = countStringInFile.countInFile;
var test = require('tape');

test('letter count function', function(t) {
  t.deepEqual(countLetters('alma'), {'a':2, 'l':1, 'm':1});
  t.end();
})
