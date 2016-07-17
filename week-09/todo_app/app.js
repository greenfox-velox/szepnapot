'use strict';

var logger = require("./logger");
var fs = require('fs');
var mysql = require("mysql");
var express = require('express');
var favicon = require('serve-favicon');
var bodyParser = require('body-parser');
var morgan = require('morgan');
var responseTime = require('response-time');
var compression = require('compression');

var app = express();
app.set('port', process.env.PORT || 3000);


var con = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "Pocok07",
  database : 'todos',
});

con.connect(function(err){
  if(err){
    console.log("Error connecting to Db");
    return;
  }
  console.log("Connection established");
});

var accessLogStream = fs.createWriteStream(__dirname + '/logs/access.log', {flags: 'a'})
logger.debug("Overriding 'Express' logger");

app.use(require('morgan')({ "stream": logger.stream }));
app.use(morgan('combined'));
app.use(favicon(__dirname + '/views/favicon.jpg'));
app.use(express.static(__dirname + '/views/'));
app.use(bodyParser.urlencoded({ extended: false}));
app.use(bodyParser.json());
app.use(responseTime());
app.use(function (req, res, next) {
  res.contentType('application/json');
  next();
});
app.use(compression({filter: shouldCompress}))

function shouldCompress(req, res) {
  if (req.headers['x-no-compression']) {
    return false
  }
  return compression.filter(req, res)
}

app.get('/todos', function(req, res) {
  con.query('SELECT * FROM tasks WHERE destroyed != "true";',function(err,rows){
    if(err) {
      console.log(err.toString());
      return;
    }
    let response = {id: rows.insertId, text:req.body.text, completed: false}
    res.json(rows);
  });
});

app.get('/todos/:id', function(req, res, next) {
  con.query('SELECT * FROM tasks WHERE id = ?;', req.params.id ,function(err,rows){
    if(err || rows.length == 0) {
      next();
      console.log(err.toString());
      return;
    }
    res.send(rows);
  });
});

app.post('/todos', function(req, res) {
  let post = {text: req.body.text}
  con.query('INSERT INTO tasks SET ?;', post,function(err,rows){
    if(err || req.body.text === undefined) {
      next();
      console.log(err.toString());
      return;
    }
    let response = {id: rows.insertId, text:req.body.text, completed: false}
    res.json(response);
  });
})

app.put('/todos/:id', function(req, res, next) {
  var query = 'UPDATE ?? SET ?? = ? WHERE ?? = ?';
  var table = ["tasks", "completed", req.body.completed, "id", req.params.id];
  query = mysql.format(query,table);
  con.query(query ,function(err,rows){
    if(err || rows.affectedRows == 0) {
      next();
      console.log(err.toString());
      return;
    }
    let response = {id: req.params.id,
                    text:req.body.text,
                    completed: req.body.completed}
    res.json(response);
  });
})

app.delete('/todos/:id', function(req, res, next) {
  var query = 'UPDATE tasks SET destroyed = true WHERE id = ? AND text = ?';
  var table = [req.params.id, req.body.text];
  query = mysql.format(query,table);
  con.query(query ,function(err,rows){
    if(err || rows.affectedRows == 0) {
      next();
      console.log(err.toString());
      return;
    }
    let response = {id: req.params.id,
                    text:req.body.text,
                    destroyed: true,
                    completed: req.body.completed}
    res.json(response);
  });
})

app.get('*', function(err, req, res, next){
  res.status(404).end('Task with given ID does not exist.');
});

app.listen(app.get('port'), function(){
  console.log('Express server listening on port ' + app.get('port'));
});
