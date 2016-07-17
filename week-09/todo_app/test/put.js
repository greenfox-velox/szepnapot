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
  describe('PUT', function() {
    var testTask = {text: "test", completed: "false"}
    it('status should be 200', function(done) {
    request(url)
  	.put('/todos/1')
  	.send(testTask)

  	.end(function(err, res) {
      if (err) {
        throw err;
      }
      should(res).have.property('status', 200);
      done();
      });
    });

    it('should send given data', function(done) {
      var testTask = {text: "test", completed: "false"}
      request(url)
      .put('/todos/1')
      .send(testTask)
      .end(function(err, res) {
        if (err) {
          throw err;
        }
        assert.ok(res);
        done();
      });
    });

    it('response contains updated task', function(done) {
      var testTask = {text: "test", completed: "true"}
      request(url)
      .put('/todos/1')
      .send(testTask)
      .end(function(err, res) {
        if (err) {
          throw err;
        }
        res.body.should.have.property('id');
        res.body.id.should.equal('1');
        res.body.should.have.property('text');
        res.body.should.have.property('completed');
        res.body.completed.should.equal('true');
        done();
      });
    });

    it('if task not found send 404', function(done) {
      var testTask = {text: "test", completed: "true"}
      request(url)
      .put('/todos/99999')
      .send(testTask)
      .end(function(err, res) {
        if (err) {
          throw err;
        }
        should(res).have.property('status', 404);
        done();
      });
    });
  });
});
