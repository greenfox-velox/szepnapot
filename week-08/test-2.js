var countBooksOfStudents = require('./02');
var test = require('tape');

var students = [
  {name: 'Steve', age: 12, books: ['Harry Potter', 'Lord of the Rings']},
  {name: 'Ryan', age: 11, books: ['The funcdation']},
  {name: 'Sheela', age: 14},
  {name: 'Charlee', age: 9, books: []},
  {name: 'Jessica', age: 12, books: ['Dune']},
  {name: 'Robert', age: 15}
];

var studentEmptyBooks = [
  {name: 'Steve', age: 12, books: []},
  {name: 'Ryan', age: 11, books: []},
  {name: 'Sheela', age: 14},
  {name: 'Charlee', age: 9, books: []},
  {name: 'Jessica', age: 12, books: []},
  {name: 'Robert', age: 15}
];

var studentNoBooksKey = [
  {name: 'Steve', age: 12},
  {name: 'Ryan', age: 11},
  {name: 'Sheela', age: 14},
  {name: 'Charlee', age: 9},
  {name: 'Jessica', age: 12},
  {name: 'Robert', age: 15}
];

test('test original example', function (t) {
  t.deepEqual(countBooksOfStudents(students), 4);
  t.end();
})

test('empty lists', function (t) {
  t.deepEqual(countBooksOfStudents(studentEmptyBooks), 0);
  t.end();
})

test('no books key', function (t) {
  t.deepEqual(countBooksOfStudents(studentNoBooksKey), 0);
  t.end();
})

test('empty object', function (t) {
  t.deepEqual(countBooksOfStudents({}), -1);
  t.end();
})
