// Import the 'request' library for making HTTP requests
const request = require('request');
// Import the 'expect' function from 'chai'
const { expect } = require('chai');

// Describe the test suite for the Index page
describe('Index page', function () {
  // Define the URL for the API endpoint
  const url = 'http://localhost:7865';

  // Test case for the correct status code
  it('should return status code 200', function (done) {
    // Make a GET request to the API
    request.get(url, (error, response, body) => {
      // Assert that the status code is 200
      expect(response.statusCode).to.equal(200);
      // Signal that the async test is complete
      done();
    });
  });

  // Test case for the correct result in the body
  it('should return the correct body content', function (done) {
    // Make a GET request to the API
    request.get(url, (error, response, body) => {
      // Assert that the body is the expected welcome message
      expect(body).to.equal('Welcome to the payment system');
      // Signal that the async test is complete
      done();
    });
  });
});
