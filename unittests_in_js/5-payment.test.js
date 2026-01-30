// Import the 'expect' function from 'chai'
const { expect } = require('chai');
// Import the 'sinon' library for creating spies
const sinon = require('sinon');
// Import the function to be tested
const sendPaymentRequestToApi = require('./5-payment.js');

// Describe the test suite for sendPaymentRequestToApi
describe('sendPaymentRequestToApi', function () {
  let consoleLogSpy;

  // Before each test, create a spy on console.log
  beforeEach(function () {
    consoleLogSpy = sinon.spy(console, 'log');
  });
  // After each test, restore the original console.log
  afterEach(function () {
    consoleLogSpy.restore();
  });
  // Test case for sendPaymentRequestToApi(100, 20)
  it('should call Utils.calculateNumber with SUM, 100, and 20', function () {
    // Call the function that we are testing
    sendPaymentRequestToApi(100, 20);

    // Assert that console.log was called with the correct message
    expect(consoleLogSpy.calledWith('The total is: 120')).to.be.true;
    // Assert that console.log was called exactly once
    expect(consoleLogSpy.calledOnce).to.be.true;
  });

  // Test case for sendPaymentRequestToApi(10, 10)
  it('should call Utils.calculateNumber with SUM, 10, and 10', function () {
    // Call the function that we are testing
    sendPaymentRequestToApi(10, 10);
    // Assert that console.log was called with the correct message
    expect(consoleLogSpy.calledWith('The total is: 20')).to.be.true;
    // Assert that console.log was called exactly once
    expect(consoleLogSpy.calledOnce).to.be.true;
  });
});
