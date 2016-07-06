'use strict';
var Car= require('./04');
var test = require('tape');

test('object created', function(t) {
  let rect = new Car("Ferarri", "red", 500);
  t.ok(rect, 'object created');
  t.end();
})
