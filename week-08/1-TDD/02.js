
'use strict';


var students = [
  {name: 'Steve', age: 12, books: ['Harry Potter', 'Lord of the Rings']},
  {name: 'Ryan', age: 11, books: ['The funcdation']},
  {name: 'Sheela', age: 14},
  {name: 'Charlee', age: 9, books: []},
  {name: 'Jessica', age: 12, books: ['Dune']},
  {name: 'Robert', age: 15}
];

// create a function that counts all the books of an array of students
// not every student has a property called books

function countBooks(studentsobj) {
  return studentsobj.reduce((result, x) => result += (x.books || []).length, 0);
}

function countBooksOfStudents(studentsobj) {
  let sumOfBooks = 0;
  if (Object.keys(studentsobj).length < 1) { return -1;}
  for (let i of studentsobj) {
    i.books ? sumOfBooks += i.books.length : 0;
  }
  return sumOfBooks;
}

module.exports = countBooksOfStudents;
