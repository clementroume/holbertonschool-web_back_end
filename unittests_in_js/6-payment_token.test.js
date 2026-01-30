// Import the 'expect' function from 'chai'
const { expect } = require('chai');
// Import the function to be tested
const getPaymentTokenFromAPI = require('./6-payment_token.js');

describe('getPaymentTokenFromAPI', function () {
  // Test case for when success is true, using the 'done' callback
  it('should return a resolved promise when success is true', function (done) {
    // Call the asynchronous function
    getPaymentTokenFromAPI(true)
      .then((response) => {
        // Assert that the response object is as expected
        expect(response).to.deep.equal({
          data: 'Successful response from the API',
        });
        // Call done() to signal that the asynchronous test is complete

        done();
      })
      .catch((error) => {
        // If the promise rejects for any reason, fail the test
        done(error);
      });
  });
});
