'use strict';

var http = require('http');
var express = require('express');

var app = express();

app.get('*', function(req, res) {
  let date = new Date();
  res.send(req.method + " Url: " + req.url + '\n' + '\n' + date);
});

app.listen(3000);
