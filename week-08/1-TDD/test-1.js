// var test = require('tape');
//
// test('basic arithmetic', function (t) {
//     t.plan(2);
//
//     t.equal(2 + 3, 5);
//     t.equal(7 * 8 + 9, 65);
// });

var countedStrings = require('./01');
var test = require('tape');

test('test for apple', function (t) {
  t.deepEqual(countedStrings('apple'), { a: 1, p: 2, l: 1, e: 1 });
  t.end();
});

test('test for spaces', function (t) {
  t.deepEqual(countedStrings('    '), { ' ': 4 });
  t.end();
});

test('test for empty string', function (t) {
  t.deepEqual(countedStrings(''), {});
  t.end();
});
