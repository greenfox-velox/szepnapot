'use strict';

function Dog( name, sound, color) {

  this.name = name;
  this.sound = sound;
  this.color = color;

};

Dog.prototype.bark = function () {
  return this.sound;
};

Dog.prototype.stats = function () {
  return "Name: " + this.name + " Sound: " + this.sound + " Color: " + this.color;
};

var fluffy = new Dog( "Yolan", "vauuu", "grey");
var doggy = new Dog( "Rudi", "wuuuf", "black");

console.log(fluffy.stats());
console.log(fluffy.bark());
console.log(doggy.stats());
console.log(doggy.bark());
