// Import the 'request' library for making HTTP requests
const request = require('request');
// Import the 'expect' function from 'chai'
const { expect } = require('chai');

// Describe the test suite for the API
describe('API integration test', function () {
  // Define the URL for the API endpoint
  const API_URL = 'http://localhost:7865';

  // Test suite for the Index page
  describe('GET /', function (done) {
    // Test case for the correct status code
    it('should return status code 200', function (done) {
      request.get(`${API_URL}/`, (error, response, body) => {
        done();
      });
    });

    // Test case for the correct result in the body
    it('should return the correct body content', function (done) {
      request.get(`${API_URL}/`, (error, response, body) => {
        expect(body).to.equal('Welcome to the payment system');
        done();
      });
    });
  });

  // Test suite for the Cart page
  describe('GET /cart/:id', function () {
    it('should return status code 200 when :id is a number', function (done) {
      request.get(`${API_URL}/cart/12`, (error, response, body) => {
        expect(response.statusCode).to.equal(200);
        expect(body).to.equal('Payment methods for cart 12');
        done();
      });
    });

    it('should return status code 404 when :id is NOT a number', function (done) {
      request.get(`${API_URL}/cart/hello`, (error, response, body) => {
        expect(response.statusCode).to.equal(404);
        done();
      });
    });
  });
});
