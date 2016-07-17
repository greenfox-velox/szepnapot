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
  describe('GET', function() {
    it('status should be 200', function(done) {
    request(url)
  	.get('/todos')
  	.send()

  	.end(function(err, res) {
      if (err) {
        throw err;
      }
      should(res).have.property('status', 200);
      done();
    });
    });

    it('should return response', function(done) {
      request(url)
      .get('/todos')
      .send()
      .end(function(err, res) {
        if (err) {
          throw err;
        }
        assert.ok(res);
        done();
      });
    });

    it('response should have id, text, completed, destroyed properties', function(done) {
      request(url)
      .get('/todos/1')
      .send()
      .end(function(err, res) {
        if (err) {
          throw err;
        }
        should(res.body[0]).have.property('id');
        should(res.body[0]).have.property('text');
        should(res.body[0]).have.property('completed');
        should(res.body[0]).have.property('destroyed');
        done();
      });
    });


    it('response header should be json', function(done) {
      request(url)
      .get('/todos/1')
      .send()
      .end(function(err, res) {
        if (err) {
          throw err;
        }
        should(res.type).equal('application/json');
        done();
      });
    });
  });
});
