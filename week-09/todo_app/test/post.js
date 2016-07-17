var should = require('should');
var assert = require('assert');
var request = require('supertest');
var winston = require('winston');
var config = require('./config');

describe('Routing', function() {
  var url = 'http://localhost:3000';

  before(function(done) {
    done();
  });
  describe('POST', function() {
    var testTask = {text: "test", completed: "false"}
    it('status should be 200', function(done) {
    request(url)
  	.post('/todos')
  	.send(testTask)

  	.end(function(err, res) {
      if (err) {
        throw err;
      }
      should(res).have.property('status', 200);
      done();
    });
    });

    it('should post given data', function(done) {
      var testTask = {text: "test", completed: "false"}
      request(url)
      .post('/todos')
      .send(testTask)
      .end(function(err, res) {
        if (err) {
          throw err;
        }
        assert.ok(res);
        done();
      });
    });


   it('respond data should have id', function(done) {
     var testTask = {text: "test", completed: "false"}
     request(url)
     .post('/todos')
     .send(testTask)
     .end(function(err, res) {
       if (err) {
         throw err;
       }
       res.body.should.have.property('id')
       done();
     });
   });

   it('request data should not overridden', function(done) {
     var testTask = {text: "test", completed: "false"}
     request(url)
     .post('/todos')
     .send(testTask)
     .end(function(err, res) {
       if (err) {
         throw err;
       }
       res.body.text.should.equal(testTask.text)
       done();
     });
   });

   it('data fetched as JSON', function(done) {
     var testTask = {text: "test", completed: "false"}
     request(url)
     .post('/todos')
     .send(testTask)
     .end(function(err, res) {
       if (err) {
         throw err;
       }
       res.req._headers['content-type'].should.equal('application/json');
       done();
     });
   })

  });
});
