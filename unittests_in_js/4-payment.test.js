// Import the 'expect' function from 'chai'
const { expect } = require('chai');
// Import the 'sinon' library for creating spies
const sinon = require('sinon');
// Import the function to be tested
const sendPaymentRequestToApi = require('./4-payment.js');
// Import the Utils module
const Utils = require('./utils.js');

// Describe the test suite for sendPaymentRequestToApi
describe('sendPaymentRequestToApi', function () {
  // Test case to verify the usage of Utils.calculateNumber
  it('should call Utils.calculateNumber with correct arguments and log the correct message', function () {
    // Stub the Utils.calculateNumber method to always return 10
    const calculateNumberStub = sinon
      .stub(Utils, 'calculateNumber')
      .returns(10);
    // Spy on console.log to monitor its calls
    const consoleLogSpy = sinon.spy(console, 'log');

    // Call the function that we are testing
    sendPaymentRequestToApi(100, 20);

    // Assert that the spy was called with the correct arguments
    expect(calculateNumberStub.calledWith('SUM', 100, 20)).to.be.true;
    // Assert that the spy was called exactly once
    expect(calculateNumberStub.calledOnce).to.be.true;

    // Assert that console.log was called with the correct message
    expect(consoleLogSpy.calledWith('The total is: 10')).to.be.true;
    // Assert that console.log was called exactly once
    expect(consoleLogSpy.calledOnce).to.be.true;

    // Restore the original method to avoid side effects in other tests
    calculateNumberStub.restore();
    consoleLogSpy.restore();
  });
});
