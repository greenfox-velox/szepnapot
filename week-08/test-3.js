'use strict';
var Rectangles= require('./03');
var test = require('tape');

test('basic example', function(t) {
  let rect = new Rectangles(5, 10);
  t.deepEqual(rect.getArea(), 50);
  t.deepEqual(rect.getCircumference(), 30);
  t.end();
})

test('object created', function(t) {
  let rect = new Rectangles(1, 1);
  t.ok(rect, 'object created');
  t.end();
})

test('negative side', function(t) {
  let rect;
  t.error(rect = new Rectangles(0, 1), "Invalid side");
  t.end();
})
