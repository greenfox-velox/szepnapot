'use strict';

// Create a constructor for creating Rectangles, it should take two parameters
// as the sides of the rectangle
// Every rectangle should have a method called getArea() that returns its area
// Every rectangle should have a method called getCircumference()
// that returns its circumference

function Rectangles(a, b) {
  if (a < 1 || b < 1) { throw "Invalid side";};
  this.a = a;
  this.b = b;
  this.getArea = function() { return this.a * this.b; }
  this.getCircumference = function() { return (this.a + this.b) * 2 ;}
}

var kicsi = new Rectangles(5, 10);

module.exports = Rectangles;
