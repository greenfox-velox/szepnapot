'use strict';

// create a student object
// that has a method `addgrade`, that takes a grade from 1 to 5
// an other method `getAverage`, that returns the average of the grades

var student = {
  grade: [],
  addgrade: function (n) { this.grade.push(n)},
  getAverage: function() { return (this.grade.reduce((a, b) => a + b, 0)) / this.grade.length}
}
student.addgrade(5);
student.addgrade(5);
student.addgrade(5);
console.log(student.getAverage());
