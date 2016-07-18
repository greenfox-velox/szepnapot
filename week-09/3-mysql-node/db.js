var mysql = require("mysql");
var express = require('express');

var con = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "Pocok07",
  database : 'bookstore',
});

con.connect(function(err){
  if(err){
    console.log("Error connecting to Db");
    return;
  }
  console.log("Connection established");
});

// con.query("SELECT book_name FROM book_mast;",function(err,rows){
//   if(err) {
//   console.log(err.toString());
//   return;
// }
//   console.log("Data received from Db:\n");
//   console.log(JSON.stringify(rows, null, 2));
// });

var app = express();

app.get('/', function(req, res) {
  con.query('SELECT book_name, aut_name, cate_descrip, book_price FROM author JOIN book_mast on book_mast.aut_id = author.aut_id JOIN category on category.cate_id = book_mast.cate_id;',function(err,rows){
    if(err) {
      console.log(err.toString());
      return;
    }
    res.send(JSON.stringify(rows, null, 2));
  });
  con.end();
});



app.listen(3000, function () {
  console.log('Example app listening on port 3000!');
});
