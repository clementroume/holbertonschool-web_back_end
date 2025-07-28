// Import the 'expect' function from 'chai'
const { expect } = require('chai');
// Import the 'sinon' library for creating spies
const sinon = require('sinon');
// Import the function to be tested
const sendPaymentRequestToApi = require('./3-payment.js');
// Import the Utils module
const Utils = require('./utils.js');

// Describe the test suite for sendPaymentRequestToApi
describe('sendPaymentRequestToApi', function () {
  // Test case to verify the usage of Utils.calculateNumber
  it('should call Utils.calculateNumber with SUM, 100, and 20', function () {
    // Create a spy on the Utils.calculateNumber method
    const calculateNumberSpy = sinon.spy(Utils, 'calculateNumber');

    // Call the function that we are testing
    sendPaymentRequestToApi(100, 20);

    // Assert that the spy was called with the correct arguments
    expect(calculateNumberSpy.calledWith('SUM', 100, 20)).to.be.true;

    // Assert that the spy was called exactly once
    expect(calculateNumberSpy.calledOnce).to.be.true;

    // Restore the original method to avoid side effects in other tests
    calculateNumberSpy.restore();
  });
});
