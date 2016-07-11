'use strict';


var fs = require('fs');

function readJSONFile(filename, callback) {
  fs.readFile(filename, function (err, data) {
    if(err) {
      callback(err);
      return;
    }
    try {
      callback(null, JSON.parse(data));
    } catch(exception) {
      callback(exception);
    }
  });
}

function writeToJSON(filename, data, callback) {
  fs.writeFile(filename,JSON.stringify( data ), 'utf8', function (err, data) {
    if(err) {
      callback(err);
      return;
    }
    try {
      callback(null, JSON.parse(data));
    } catch(exception) {
      callback(exception);
    }
  });
}

function init(){
  readJSONFile('data.json', function(err, cont) {
    if (err) { console.log(err);; }
    data = cont;
  })
}

function save(object){
  writeToJSON('data.json', object, function(err, cont) {
    if (err) { console.log(err); }
    console.log('saved');
  })
}

var data;
init();

var express = require('express');
var bodyParser = require('body-parser');
var app = express();
var path = require('path');

app.use(express.static(__dirname + '/views/'));
app.use(bodyParser.urlencoded({ extended: false}));
app.use(bodyParser.json());
app.use(function (req, res, next) {
  res.contentType('application/json');
  next();
});


app.get('/todos', function(req, res) {
  res.json(data.filter(function(item){ return !item.destroyed || undefined;}));
});

app.get('/todos/:id', function(req, res) {
  res.json(data.filter(function(item){ return item.id === +req.params.id;}));
});

app.post('/todos', function(req, res) {
  req.body.completed = false;
  req.body.id = data.length + 1;
  data.push(req.body);
  save(data);
  res.json(req.body);
})

app.put('/todos/:id', function(req, res, next) {
  let taskIndex = data.indexOf(data.filter(function(item){ return item.id === +req.params.id;})[0]);
  if (taskIndex < 0) { return next(true); }
  data[taskIndex].completed = req.body.completed ;
  data[taskIndex].text = req.body.text;
  save(data);
  res.json(data[taskIndex]);
})

app.delete('/todos/:id', function(req, res, next) {
  let taskIndex = data.indexOf(data.filter(function(item){ return item.id === +req.params.id;})[0]);
  if (taskIndex < 0) { return next(true); }
  data[taskIndex].destroyed = true;
  save(data);
  res.json(data[taskIndex]);
})

app.use(function(err, req, res, next) {
   res.sendStatus(404);
});

app.listen(3000);
