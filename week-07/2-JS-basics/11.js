'use strict';

// Create a `Stack` constructor that stores elements
// It should have a `size` method that returns number of elements it has
// It should have a `push` method that adds an element to the stack
// It should have a `pop` method that returns the last element form the stack and also deletes it from it

// please don`t use the built in methods

function Stack(arr) {
  this.array = arr;
  this.size = function () { return this.array.length};
  this.push = function (item) { arr[length] = item };
  this.pop = function () { var lastElement = arr[arr.length - 1]; delete arr[lastElement]; return lastElement}
}

console.log(new Stack([1, 2, 3, 4]).size());
