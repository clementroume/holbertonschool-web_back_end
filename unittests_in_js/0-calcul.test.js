// Import the 'assert' module for assertions
const assert = require('assert');
// Import the function to be tested
const calculateNumber = require('./0-calcul.js');
assert;

// Describe the test suite for the calculateNumber function
describe('calculateNumber', function () {
  // Test case 1: Basic integers
  it('should return 4 when inputs are 1 and 3', function () {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });

  // Test case 2: One number needs rounding up
  it('should return 5 when inputs are 1 and 3.7', function () {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });

  // Test case 3: Both numbers need rounding up
  it('should return 6 when inputs are 1.5 and 3.7', function () {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });

  // Test case 4: One number rounds down, one rounds up
  it('should return 5 when inputs are 1.2 and 3.7', function () {
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
  });

  // Test case 5: Both numbers round down
  it('should return 4 when inputs are 1.2 and 3.2', function () {
    assert.strictEqual(calculateNumber(1.2, 3.2), 4);
  });

  // Test case 6: Zero values
  it('should return 0 when inputs are 0 and 0', function () {
    assert.strictEqual(calculateNumber(0, 0), 0);
  });

  // Test case 7: Negative numbers
  it('should return -4 when inputs are -1 and -3', function () {
    assert.strictEqual(calculateNumber(-1, -3), -4);
  });

  // Test case 8: Negative numbers with rounding
  it('should return -5 when inputs are -1 and -3.7', function () {
    assert.strictEqual(calculateNumber(-1, -3.7), -5);
  });

  // Test case 9: Negative numbers with rounding down
  it('should return -5 when inputs are -1.2 and -3.7', function () {
    assert.strictEqual(calculateNumber(-1.2, -3.7), -5);
  });

  // Test case 10: Negative numbers with rounding up
  it('should return -4 when inputs are -1.5 and -3.2', function () {
    assert.strictEqual(calculateNumber(-1.5, -3.2), -4);
  });

  // Test case 11: Mixed positive and negative numbers
  it('should return 2 when inputs are -1 and 3', function () {
    assert.strictEqual(calculateNumber(-1, 3), 2);
  });

  // Test case 12: Mixed numbers with rounding
  it('should return 3 when inputs are -1.5 and 3.7', function () {
    assert.strictEqual(calculateNumber(-1.5, 3.7), 3);
  });
});
